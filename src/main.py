import argparse

from commands import add
# Create argument parser
parser = argparse.ArgumentParser(prog="CLI task tracker")

# Add arguments to parser
parser.add_argument("-a", '--add', type=str, help="Add a new task")
parser.add_argument('-u', '--update',nargs=2, help="Update an existing task only")
parser.add_argument('-d', '--delete', type=int, help="Delete an existing task only")
parser.add_argument('--mark-in-progress', type=int, help="Mark-in-progress an existing task only")
parser.add_argument('--mark-done', type=int, help='Mark-done an existing task only')
parser.add_argument('--list', nargs="?",type=str, help="List all / List done / List todo / List in-progress")

# Parse the arguments
args = parser.parse_args()

if __name__ == "__main__":
    if args.add:
        add(args.add)