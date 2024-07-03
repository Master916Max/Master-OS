class Bcolors:
    # Foreground colors
    HEADER = '\033[95m'         # Light magenta (light purple/pink)
    OKBLUE = '\033[94m'         # Light blue
    OKCYAN = '\033[96m'         # Light cyan (light aqua)
    OKGREEN = '\033[92m'        # Light green
    WARNING = '\033[93m'        # Yellow
    FAIL = '\033[91m'           # Light red
    ENDC = '\033[0m'            # Reset to default
    BOLD = '\033[1m'            # Bold text
    UNDERLINE = '\033[4m'       # Underlined text
    BLACK = '\033[30m'          # Black
    RED = '\033[31m'            # Red
    GREEN = '\033[32m'          # Green
    YELLOW = '\033[33m'         # Yellow
    BLUE = '\033[34m'           # Blue
    MAGENTA = '\033[35m'        # Magenta (dark pink/purple)
    CYAN = '\033[36m'           # Cyan (aqua)
    WHITE = '\033[37m'          # White
    LIGHTBLACK = '\033[90m'     # Bright black (grey)
    LIGHTRED = '\033[91m'       # Bright red
    LIGHTGREEN = '\033[92m'     # Bright green
    LIGHTYELLOW = '\033[93m'    # Bright yellow
    LIGHTBLUE = '\033[94m'      # Bright blue
    LIGHTMAGENTA = '\033[95m'   # Bright magenta (bright purple/pink)
    LIGHTCYAN = '\033[96m'      # Bright cyan (bright aqua)
    LIGHTWHITE = '\033[97m'     # Bright white

    # Background colors
    BG_BLACK = '\033[40m'       # Black background
    BG_RED = '\033[41m'         # Red background
    BG_GREEN = '\033[42m'       # Green background
    BG_YELLOW = '\033[43m'      # Yellow background
    BG_BLUE = '\033[44m'        # Blue background
    BG_MAGENTA = '\033[45m'     # Magenta background (dark pink/purple)
    BG_CYAN = '\033[46m'        # Cyan background (aqua)
    BG_WHITE = '\033[47m'       # White background
    BG_LIGHTBLACK = '\033[100m' # Bright black (grey) background
    BG_LIGHTRED = '\033[101m'   # Bright red background
    BG_LIGHTGREEN = '\033[102m' # Bright green background
    BG_LIGHTYELLOW = '\033[103m'# Bright yellow background
    BG_LIGHTBLUE = '\033[104m'  # Bright blue background
    BG_LIGHTMAGENTA = '\033[105m' # Bright magenta background (bright purple/pink)
    BG_LIGHTCYAN = '\033[106m'  # Bright cyan background (bright aqua)
    BG_LIGHTWHITE = '\033[107m' # Bright white background

    # Additional formatting
    STRIKETHROUGH = '\033[9m'   # Strikethrough text
    ITALIC = '\033[3m'          # Italic text
    REVERSED = '\033[7m'        # Reversed foreground and background colors
    CONCEAL = '\033[8m'         # Concealed text (invisible)
    OVERLINE = '\033[53m'       # Overlined text
    BLINK = '\033[5m'           # Blinking text
    DOUBLE_UNDERLINE = '\033[21m' # Double underline text
    FRAMED = '\033[51m'         # Framed text
    CIRCLED = '\033[52m'        # Circled text
    FAINT = '\033[2m'           # Faint (dim) text

    # Extended colors (may not be supported universally)
    ORANGE = '\033[38;5;208m'   # Orange color
    PINK = '\033[38;5;205m'     # Pink color
    PURPLE = '\033[38;5;171m'   # Purple color
    DARK_GREEN = '\033[38;5;22m' # Dark green color
    LIGHT_ORANGE = '\033[38;5;215m' # Light orange color
    DARK_BLUE = '\033[38;5;19m' # Dark blue color
    GREY = '\033[38;5;243m'     # Grey color
    BROWN = '\033[38;5;130m'    # Brown color
    OLIVE = '\033[38;5;142m'    # Olive color
    GOLD = '\033[38;5;220m'     # Gold color
    DARK_PURPLE = '\033[38;5;90m' # Dark purple color
    INDIGO = '\033[38;5;54m'    # Indigo color
    TEAL = '\033[38;5;37m'      # Teal color
    MAROON = '\033[38;5;52m'    # Maroon color
    LIME = '\033[38;5;154m'     # Lime color
    SKY_BLUE = '\033[38;5;111m' # Sky blue color

# Example usage
if __name__ == "__main__":
    print(f"{Bcolors.HEADER}Header Text{Bcolors.ENDC}")
    print(f"{Bcolors.OKBLUE}Blue Text{Bcolors.ENDC}")
    print(f"{Bcolors.OKCYAN}Cyan Text{Bcolors.ENDC}")
    print(f"{Bcolors.OKGREEN}Green Text{Bcolors.ENDC}")
    print(f"{Bcolors.WARNING}Warning Text{Bcolors.ENDC}")
    print(f"{Bcolors.FAIL}Fail Text{Bcolors.ENDC}")
    print(f"{Bcolors.BOLD}Bold Text{Bcolors.ENDC}")
    print(f"{Bcolors.UNDERLINE}Underlined Text{Bcolors.ENDC}")
    print(f"{Bcolors.BLACK}Black Text{Bcolors.ENDC}")
    print(f"{Bcolors.RED}Red Text{Bcolors.ENDC}")
    print(f"{Bcolors.GREEN}Green Text{Bcolors.ENDC}")
    print(f"{Bcolors.YELLOW}Yellow Text{Bcolors.ENDC}")
    print(f"{Bcolors.BLUE}Blue Text{Bcolors.ENDC}")
    print(f"{Bcolors.MAGENTA}Magenta Text{Bcolors.ENDC}")
    print(f"{Bcolors.CYAN}Cyan Text{Bcolors.ENDC}")
    print(f"{Bcolors.WHITE}White Text{Bcolors.ENDC}")
    print(f"{Bcolors.LIGHTBLACK}Bright Black (Grey) Text{Bcolors.ENDC}")
    print(f"{Bcolors.LIGHTRED}Bright Red Text{Bcolors.ENDC}")
    print(f"{Bcolors.LIGHTGREEN}Bright Green Text{Bcolors.ENDC}")
    print(f"{Bcolors.LIGHTYELLOW}Bright Yellow Text{Bcolors.ENDC}")
    print(f"{Bcolors.LIGHTBLUE}Bright Blue Text{Bcolors.ENDC}")
    print(f"{Bcolors.LIGHTMAGENTA}Bright Magenta Text{Bcolors.ENDC}")
    print(f"{Bcolors.LIGHTCYAN}Bright Cyan Text{Bcolors.ENDC}")
    print(f"{Bcolors.LIGHTWHITE}Bright White Text{Bcolors.ENDC}")
    print(f"{Bcolors.BG_BLACK}{Bcolors.WHITE}Black Background with White Text{Bcolors.ENDC}")
    print(f"{Bcolors.BG_RED}{Bcolors.WHITE}Red Background with White Text{Bcolors.ENDC}")
    print(f"{Bcolors.BG_GREEN}{Bcolors.BLACK}Green Background with Black Text{Bcolors.ENDC}")
    print(f"{Bcolors.BG_YELLOW}{Bcolors.BLACK}Yellow Background with Black Text{Bcolors.ENDC}")
    print(f"{Bcolors.BG_BLUE}{Bcolors.WHITE}Blue Background with White Text{Bcolors.ENDC}")
    print(f"{Bcolors.BG_MAGENTA}{Bcolors.BLACK}Magenta Background with Black Text{Bcolors.ENDC}")
    print(f"{Bcolors.BG_CYAN}{Bcolors.BLACK}Cyan Background with Black Text{Bcolors.ENDC}")
    print(f"{Bcolors.BG_WHITE}{Bcolors.BLACK}White Background with Black Text{Bcolors.ENDC}")
    print(f"{Bcolors.BG_LIGHTBLACK}{Bcolors.WHITE}Bright Black (Grey) Background with White Text{Bcolors.ENDC}")
    print(f"{Bcolors.BG_LIGHTRED}{Bcolors.WHITE}Bright Red Background with White Text{Bcolors.ENDC}")
    print(f"{Bcolors.BG_LIGHTGREEN}{Bcolors.BLACK}Bright Green Background with Black Text{Bcolors.ENDC}")
    print(f"{Bcolors.BG_LIGHTYELLOW}{Bcolors.BLACK}Bright Yellow Background with Black Text{Bcolors.ENDC}")
    print(f"{Bcolors.BG_LIGHTBLUE}{Bcolors.BLACK}Bright Blue Background with Black Text{Bcolors.ENDC}")
    print(f"{Bcolors.BG_LIGHTMAGENTA}{Bcolors.BLACK}Bright Magenta Background with Black Text{Bcolors.ENDC}")
    print(f"{Bcolors.BG_LIGHTCYAN}{Bcolors.BLACK}Bright Cyan Background with Black Text{Bcolors.ENDC}")
    print(f"{Bcolors.BG_LIGHTWHITE}{Bcolors.BLACK}Bright White Background with Black Text{Bcolors.ENDC}")
    print(f"{Bcolors.ITALIC}Italic Text{Bcolors.ENDC}")
    print(f"{Bcolors.STRIKETHROUGH}Strikethrough Text{Bcolors.ENDC}")
    print(f"{Bcolors.REVERSED}Reversed Colors Text{Bcolors.ENDC}")
    print(f"{Bcolors.CONCEAL}Concealed Text (Invisible){Bcolors.ENDC}")
    print(f"{Bcolors.OVERLINE}Overlined Text{Bcolors.ENDC}")
    print(f"{Bcolors.BLINK}Blinking Text{Bcolors.ENDC}")
    print(f"{Bcolors.DOUBLE_UNDERLINE}Double Underlined Text{Bcolors.ENDC}")
    print(f"{Bcolors.FRAMED}Framed Text{Bcolors.ENDC}")
    print(f"{Bcolors.CIRCLED}Circled Text{Bcolors.ENDC}")
    print(f"{Bcolors.FAINT}Faint (Dim) Text{Bcolors.ENDC}\n\n\n")

    # Extended colors
    print(f"{Bcolors.ORANGE}Orange Text{Bcolors.ENDC}")
    print(f"{Bcolors.PINK}Pink Text{Bcolors.ENDC}")
    print(f"{Bcolors.PURPLE}Purple Text{Bcolors.ENDC}")
    print(f"{Bcolors.DARK_GREEN}Dark Green Text{Bcolors.ENDC}")
    print(f"{Bcolors.LIGHT_ORANGE}Light Orange Text{Bcolors.ENDC}")
    print(f"{Bcolors.DARK_BLUE}Dark Blue Text{Bcolors.ENDC}")
    print(f"{Bcolors.GREY}Grey Text{Bcolors.ENDC}")
    print(f"{Bcolors.BROWN}Brown Text{Bcolors.ENDC}")
    print(f"{Bcolors.OLIVE}Olive Text{Bcolors.ENDC}")
    print(f"{Bcolors.GOLD}Gold Text{Bcolors.ENDC}")
    print(f"{Bcolors.DARK_PURPLE}Dark Purple Text{Bcolors.ENDC}")
    print(f"{Bcolors.INDIGO}Indigo Text{Bcolors.ENDC}")
    print(f"{Bcolors.TEAL}Teal Text{Bcolors.ENDC}")
    print(f"{Bcolors.MAROON}Maroon Text{Bcolors.ENDC}")
    print(f"{Bcolors.LIME}Lime Text{Bcolors.ENDC}")
    print(f"{Bcolors.SKY_BLUE}Sky Blue Text{Bcolors.ENDC}")

class Emojis:
    SMILE = "😊"
    HEART = "❤️"
    LAUGH = "😂"
    THINKING = "🤔"
    CLAP = "👏"
    THUMBS_UP = "👍"
    THUMBS_DOWN = "👎"
    FIRE = "🔥"
    ROCKET = "🚀"
    HOURGLASS = "⌛"
    CHECK_MARK = "✔️"
    CROSS_MARK = "❌"
    WARNING = "⚠️"
    LIGHTBULB = "💡"
    BOOK = "📖"
    MAGNIFYING_GLASS = "🔍"
    TELESCOPE = "🔭"
    CALENDAR = "📅"
    CAMERA = "📷"
    FILM_CAMERA = "🎥"
    STAR = "⭐"
    CLOUD = "☁️"
    SUN = "☀️"
    MOON = "🌙"
    UMBRELLA = "☂️"
    RAINBOW = "🌈"
    SNOWFLAKE = "❄️"
    TORNADO = "🌪️"
    EARTH_GLOBE = "🌍"
    ALIEN = "👽"
    CAT = "🐱"
    DOG = "🐶"
    FISH = "🐟"
    TURTLE = "🐢"
    SPIDER = "🕷️"
    SCORPION = "🦂"
    BUG = "🐛"
    BEE = "🐝"
    ANT = "🐜"
    LADY_BEETLE = "🐞"
    SNAKE = "🐍"
    ELEPHANT = "🐘"
    PANDA = "🐼"
    TIGER = "🐅"
    PIG = "🐖"
    CHICKEN = "🐔"
    HORSE = "🐴"
    SHEEP = "🐑"
    COW = "🐄"
    WHALE = "🐋"
    DOLPHIN = "🐬"
    OCTOPUS = "🐙"
    CRAB = "🦀"
    SHIP = "🚢"
    CAR = "🚗"
    BUS = "🚌"
    AIRPLANE = "✈️"
    BICYCLE = "🚲"
    TRAIN = "🚂"
    ROCKET_SHIP = "🚀"
    HOUSE_BUILDING = "🏠"
    FACTORY = "🏭"
    STATUE_OF_LIBERTY = "🗽"
    CROWN = "👑"
    GIFT = "🎁"
    CHRISTMAS_TREE = "🎄"
    BIRTHDAY_CAKE = "🎂"
    FOOTPRINTS = "👣"
    KEY = "🔑"
    LOCK = "🔒"
    UNLOCK = "🔓"
    MAILBOX = "📫"
    MAG = "🔍"
    TELESCOPE = "🔭"
    CALENDAR = "📅"
    CAMERA = "📷"
    FILM_CAMERA = "🎥"
    HORIZONTAL_LINE = "─"
    VERTICAL_LINE = "│"
    UP_DOWN_ARROW = "↕️"
    LEFT_RIGHT_ARROW = "↔️"
    DOUBLE_VERTICAL_LINE = "║"
    DOUBLE_HORIZONTAL_LINE = "═"
    CROSS = "✝️"
    DIAGONAL_UP_SLASH = "↗️"
    DIAGONAL_DOWN_SLASH = "↘️"
    SMILEY_FACE = "🙂"
    SAD_FACE = "☹️"
    WINK_FACE = "😉"
    GRINNING_FACE = "😀"
    KISSING_FACE = "😗"
    CRYING_FACE = "😢"
    ANGRY_FACE = "😡"

    @classmethod
    def print_all(cls):
        emojis = [getattr(cls, attr) for attr in dir(cls) if not callable(getattr(cls, attr)) and not attr.startswith("__")]
        for emoji in emojis:
            print(emoji, end="\n")
        print()
