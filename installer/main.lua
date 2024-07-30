local screens = {}
local currentScreen = "welcome"
local previousScreen = nil

local installLocation = ""
local editionSelection = "N" -- Standardmäßig auf "N" setzen
local features = {}
local autoUpdate = false
local installProgress = 0
local installing = false
local showSummary = false -- Steuerung, ob die Zusammenfassung angezeigt wird oder nicht
local typingLocation = false -- Variable zur Steuerung der Texteingabe

-- Globale Listen für Features je nach Edition (Not Finsished)
local editionFeatures = {
    N = {"Browser", "GUI"},
    P = {"Browser", "GUI", "Spiele"},
    E = {"Browser", "GUI", "Spiele", "Debugging SW"}
}

-- Logos für jede Edition
local logos = {}

-- Button-Klasse
local Button = {}
Button.__index = Button

function Button.new(x, y, width, height, label, action)
    local self = setmetatable({}, Button)
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.label = label
    self.action = action
    return self
end

function Button:draw()
    love.graphics.setColor(0.2, 0.2, 0.2)
    love.graphics.rectangle("fill", self.x, self.y, self.width, self.height)
    love.graphics.setColor(1, 1, 1)
    love.graphics.printf(self.label, self.x, self.y + self.height / 2 - 10, self.width, "center")
end

function Button:isClicked(mx, my)
    return mx >= self.x and mx <= self.x + self.width and my >= self.y and my <= self.y + self.height
end

-- Kreis-Klasse für Feature-Auswahl
local Circle = {}
Circle.__index = Circle

function Circle.new(x, y, radius, feature)
    local self = setmetatable({}, Circle)
    self.x = x
    self.y = y
    self.radius = radius
    self.feature = feature
    return self
end

function Circle:draw()
    love.graphics.setColor(1, 1, 1)
    love.graphics.circle("line", self.x, self.y, self.radius)
    if features[self.feature] then
        love.graphics.setColor(0, 0.8, 0)
        love.graphics.circle("fill", self.x, self.y, self.radius - 4)
    end
    love.graphics.setColor(1, 1, 1)
end

function Circle:isClicked(mx, my)
    local dx = mx - self.x
    local dy = my - self.y
    return dx * dx + dy * dy <= self.radius * self.radius
end

-- Menü-Initialisierung
function initScreens()
    local screenWidth, screenHeight = love.graphics.getDimensions()

    screens["welcome"] = {
        buttons = {
            Button.new(screenWidth / 2 - 100, screenHeight / 2 - 25, 200, 50, "Start", function() changeScreen("editionSelection") end)
        }
    }

    screens["editionSelection"] = {
        buttons = {
            Button.new(screenWidth / 2 - 100, screenHeight / 2 - 75, 200, 50, "Normal", function() editionSelection = "N"; changeScreen("locationSelection") end),
            Button.new(screenWidth / 2 - 100, screenHeight / 2 - 15, 200, 50, "Premium", function() editionSelection = "P"; changeScreen("locationSelection") end),
            Button.new(screenWidth / 2 - 100, screenHeight / 2 + 45, 200, 50, "Exclusive", function() editionSelection = "E"; changeScreen("locationSelection") end)
        }
    }

    screens["locationSelection"] = {
        buttons = {
            Button.new(screenWidth / 2 - 100, screenHeight / 2 - 25, 200, 50, "Installationsort: " .. (installLocation ~= "" and installLocation or "Nicht festgelegt"), function() 
                selectFolder()
            end),
            Button.new(screenWidth / 2 - 100, screenHeight / 2 + 35, 200, 50, "Weiter", function() 
                changeScreen("featureSelection")
            end),
            Button.new(screenWidth / 2 - 100, screenHeight / 2 + 95, 200, 50, "Zurück", function() 
                changeScreen("editionSelection") 
            end)
        }
    }

    screens["featureSelection"] = {
        buttons = {},
        circles = {},
        initialize = function()
            -- Dynamisch Features für die ausgewählte Edition hinzufügen
            local featureButtons = {}
            local featureCircles = {}
            local startY = screenHeight / 2 - (#editionFeatures[editionSelection] * 60) / 2
            for i, feature in ipairs(editionFeatures[editionSelection]) do
                table.insert(featureButtons, Button.new(screenWidth / 2 - 50, startY + (i - 1) * 60, 200, 50, feature, function()
                    features[feature] = not features[feature]
                end))
                table.insert(featureCircles, Circle.new(screenWidth / 2 - 100, startY + (i - 1) * 60 + 25, 15, feature))
            end
            -- Bestätigen Button
            table.insert(featureButtons, Button.new(screenWidth / 2 - 100, startY + (#editionFeatures[editionSelection]) * 60 + 60, 200, 50, "Bestätigen", function() changeScreen("autoUpdate") end))
            -- Zurück Button
            table.insert(featureButtons, Button.new(screenWidth / 2 - 100, startY + (#editionFeatures[editionSelection]) * 60 + 120, 200, 50, "Zurück", function() changeScreen("locationSelection") end))
            screens["featureSelection"].buttons = featureButtons
            screens["featureSelection"].circles = featureCircles
        end
    }

    screens["autoUpdate"] = {
        buttons = {
            Button.new(screenWidth / 2 - 100, screenHeight / 2 - 25, 200, 50, "Ja", function() autoUpdate = true; changeScreen("summary") end),
            Button.new(screenWidth / 2 - 100, screenHeight / 2 + 35, 200, 50, "Nein", function() autoUpdate = false; changeScreen("summary") end),
            Button.new(screenWidth / 2 - 100, screenHeight / 2 + 95, 200, 50, "Zurück", function() changeScreen("featureSelection") end)
        }
    }

    screens["summary"] = {
        buttons = {
            Button.new(screenWidth / 2 - 100, screenHeight / 2 - 25, 200, 50, "Zeige Zusammenfassung", function() showSummary = true end),
            Button.new(screenWidth / 2 - 100, screenHeight / 2 + 35, 200, 50, "Weiter", function() showSummary = false; changeScreen("installer") end),
            Button.new(screenWidth / 2 - 100, screenHeight / 2 + 95, 200, 50, "Zurück", function() changeScreen("autoUpdate") end)
        }
    }

    screens["displaySummary"] = {
        buttons = {
            Button.new(screenWidth / 2 - 100, screenHeight / 2 + 100, 200, 50, "Schließen", function() showSummary = false; changeScreen("summary") end),
            Button.new(screenWidth / 2 - 100, screenHeight / 2 + 160, 200, 50, "Weiter", function() showSummary = false; changeScreen("installer") end)
        }
    }

    screens["installer"] = {
        buttons = {
            Button.new(screenWidth / 2 - 100, screenHeight / 2 - 25, 200, 50, "Installation starten", function() startInstallation() end),
            Button.new(screenWidth / 2 - 100, screenHeight / 2 + 35, 200, 50, "Abbrechen", function() love.event.quit() end)
        }
    }
end

-- Bildschirmwechsel
function changeScreen(newScreen)
    if screens[newScreen].initialize then
        screens[newScreen]:initialize()
    end
    previousScreen = currentScreen
    currentScreen = newScreen
end

-- Installation starten
function startInstallation()
    installing = true
    installProgress = 0
end

-- Installationsfortschritt aktualisieren
function updateInstallation(dt)
    if installing then
        installProgress = installProgress + dt * 10 -- Simulierte Installationsgeschwindigkeit
        if installProgress >= 100 then
            installProgress = 100
            installing = false
        end
    end
end

-- Hauptprogramm
function love.load()
    love.window.setMode(0, 0, {fullscreen = true}) -- Vollbildmodus
    love.graphics.setBackgroundColor(0.2, 0.6, 1) -- Ein schönes Blau

    -- Logos laden
    --logos.N = love.graphics.newImage("/Logos/MOS-Logo.png")
    --logos.P = love.graphics.newImage("/Logos/MOS-Logo-P.png")
    --logos.E = love.graphics.newImage("/Logos/MOS-Logo-E.png")

    initScreens()
end

-- Update-Funktion
function love.update(dt)
    updateInstallation(dt)
end

-- Zeichnen
function love.draw()
    -- Hintergrundfarbe setzen
    love.graphics.clear(0.2, 0.6, 1) -- Ein schönes Blau

    -- Aktuelles Logo basierend auf der ausgewählten Edition anzeigen
    local currentLogo = logos[editionSelection]
    if currentLogo then
        love.graphics.draw(currentLogo, love.graphics.getWidth() / 2 - currentLogo:getWidth() / 4, 10, 0, 0.5, 0.5)
    end

    if showSummary then
        -- Popup-Hintergrund
        love.graphics.setColor(0, 0, 0, 0.8) -- Schwarz mit Transparenz
        love.graphics.rectangle("fill", love.graphics.getWidth() / 4, love.graphics.getHeight() / 4, love.graphics.getWidth() / 2, love.graphics.getHeight() / 2)

        -- Temporäre Schriftart speichern und ändern
        local originalFont = love.graphics.getFont()
        local popupFont = love.graphics.newFont(20)
        love.graphics.setFont(popupFont)

        -- Zusammenfassungsinformationen
        love.graphics.setColor(1, 1, 1) -- Weiß
        love.graphics.printf("Zusammenfassung der Installation:\n\nEdition: " .. editionSelection .. "\nInstallationsort: " .. installLocation .. "\nAutomatische Updates: " .. (autoUpdate and "Ja" or "Nein") .. "\nFeatures: " .. table.concat(editionFeatures[editionSelection], ", "), love.graphics.getWidth() / 4 + 20, love.graphics.getHeight() / 4 + 20, love.graphics.getWidth() / 2 - 40)

        -- Buttons für die Zusammenfassung anzeigen
        for _, button in ipairs(screens["displaySummary"].buttons) do
            button:draw()
        end

        -- Schriftart zurücksetzen
        love.graphics.setFont(originalFont)
    else
        -- Buttons und Kreise für den aktuellen Bildschirm anzeigen
        for _, button in ipairs(screens[currentScreen].buttons) do
            button:draw()
        end
        if screens[currentScreen].circles then
            for _, circle in ipairs(screens[currentScreen].circles) do
                circle:draw()
            end
        end
    end

    -- Installationsfortschritt anzeigen
    if installing then
        love.graphics.setColor(0.8, 0.8, 0.8)
        love.graphics.rectangle("fill", love.graphics.getWidth() / 4, love.graphics.getHeight() - 100, love.graphics.getWidth() / 2, 30)
        love.graphics.setColor(0.2, 0.8, 0.2)
        love.graphics.rectangle("fill", love.graphics.getWidth() / 4, love.graphics.getHeight() - 100, (love.graphics.getWidth() / 2) * (installProgress / 100), 30)
        love.graphics.setColor(1, 1, 1)
        love.graphics.printf("Installation: " .. math.floor(installProgress) .. "%", love.graphics.getWidth() / 4, love.graphics.getHeight() - 95, love.graphics.getWidth() / 2, "center")
    end
end

-- Texteingabe-Handler
function love.textinput(t)
    if typingLocation then
        installLocation = installLocation .. t
        -- Update des Buttons
        screens["locationSelection"].buttons[1].label = "Installationsort: " .. installLocation
    end
end

-- Tasten-Handler
function love.keypressed(key)
    if typingLocation and key == "backspace" then
        -- Entferne das letzte Zeichen
        installLocation = installLocation:sub(1, -2)
        -- Update des Buttons
        screens["locationSelection"].buttons[1].label = "Installationsort: " .. installLocation
    end
end

-- Mausereignis
function love.mousepressed(x, y, button)
    if button == 1 then -- Linksklick
        if showSummary then
            for _, btn in ipairs(screens["displaySummary"].buttons) do
                if btn:isClicked(x, y) then
                    btn.action()
                    break
                end
            end
        else
            for _, btn in ipairs(screens[currentScreen].buttons) do
                if btn:isClicked(x, y) then
                    btn.action()
                    break
                end
            end
            if screens[currentScreen].circles then
                for _, circle in ipairs(screens[currentScreen].circles) do
                    if circle:isClicked(x, y) then
                        features[circle.feature] = not features[circle.feature]
                        break
                    end
                end
            end
        end
    end
end

-- Funktion zur Auswahl des Ordners
function selectFolder()
    -- Dies ist ein Platzhalter für die Ordnerauswahl. 
    -- Sie können eine benutzerdefinierte Lösung mit `lfs` oder einem Drittanbieter-Tool implementieren.
    -- Zum Beispiel: Ein einfacher Dateidialog könnte mit einem externen Tool wie zenity erstellt werden.
    -- Hier nehmen wir einfach einen statischen Ordnerpfad für das Beispiel.
    installLocation = "/Beispiel/Installationsordner"
    screens["locationSelection"].buttons[1].label = "Installationsort: " .. installLocation
end
