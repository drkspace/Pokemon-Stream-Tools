from botCommands import Bot
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Twitch Bot.')
    parser.add_argument('token', metavar='oauth:xxx', type=str,
                        help='The twitch authentication token')
    parser.add_argument('client_id', metavar='xxx', type=str,
                        help='The twitch app client ID.')
    parser.add_argument('channel', metavar='Channel Name', type=str,
                        help='The channel name for the bot to be in.')

    return parser.parse_args()


def main(args):
    bot = Bot(
        # set up the bot
        token=args.token,
        client_id=args.client_id,
        prefix="!",
        initial_channels=[args.channel]
    )

    bot.run()


if __name__ == "__main__":

    args = parse_arguments()
    main(args)
