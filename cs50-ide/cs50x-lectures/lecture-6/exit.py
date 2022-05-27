# show exit statuses
import sys

if len(sys.argv) != 2:
    print('missing command-line argument')
    # Exit with a code of 1
    sys.exit(1)

print(f'hello, {sys.argv[1]}')
# Exit with a code of 0
sys.exit(0)