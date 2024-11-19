import argparse
import sys

from commands import add, update, delete, mark_in_progress, mark_done, list_task, list_all_task
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
        
    if args.update:
        # Unpacking the two arguments given
        id_arg, description_arg = args.update
        while True:
            prompt_update = input("Are you sure you want to update task [Y/N]?: ")
            if prompt_update in ["Y", "y"]:
                update(int(id_arg), description_arg)
                break
            elif prompt_update in ["N", "n"]:
                sys.exit(0)
            else:
                print("Wrong input please type [Y/N]")

    if args.delete:
        while True:
            prompt_delete = input("Are you sure you want to delete task [Y/N]?: ")
            if prompt_delete in ["Y", "y"]:
                delete(args.delete)
                break
            elif prompt_delete in ["N", "n"]:
                sys.exit(0)
            else:
                print("Wrong input please type [Y/N]")

    if args.mark_in_progress:
        mark_in_progress(args.mark_in_progress)

    if args.mark_done:
        mark_done(args.mark_done)

    if args.list is None:
        list_all_task()
    else:
        list_task(args.list)