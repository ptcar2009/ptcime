from .parsing import main_parser
from .time_tracking import start, stop, week, day

if __name__ == "__main__":
    arguments = main_parser.parse_args()
    if arguments.action == "start":
        start()
    if arguments.action == "stop":
        stop()
    if arguments.action == "week":
        week()
    if arguments.action == "day":
        day()