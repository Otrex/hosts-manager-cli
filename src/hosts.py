import argparse
from src.model import Describers

class CommandParser:
    def __init__(self):
        self.handlers = {}
        self.parser = argparse.ArgumentParser(description='Manage Your Local Domains')
        self.subparsers = self.parser.add_subparsers(title='Commands', dest='command')

    def generate(self, model):
        for subparser in model:
            add_parser = self.subparsers.add_parser(subparser[0], **subparser[1])
            self.handlers[subparser[0]] = subparser[3]

            for argument in subparser[2]:
                add_parser.add_argument(argument[0], **argument[1])

    def run(self):
        try:
            args = self.parser.parse_args()
            method = self.handlers[args.command]
            method(**getattr(args, "__dict__"))
        except KeyError:
            self.parser.print_help()

    @staticmethod
    def start():
        commander = CommandParser()
        commander.generate(Describers)
        commander.run()


if __name__ == '__main__':
    CommandParser.start()
