''''python module to read a file line by line and does some processing and write in a different file'''
import sys

def main(argv):

    in_file = open(str(sys.argv[1]), 'r')
    out_file = open(sys.argv[2] + "_log.txt", 'w')
    error_file = open(sys.argv[2] + "_error.txt", 'w')

    while True:
        line = in_file.readline()
        if not line:
            break
        if (line.find(sys.argv[2]) != -1):
            '''print(line)'''
            out_file.write(line)
            if (line.find('ERROR') != -1  or line.find('WARNING') != -1):
                error_file.write(line)

    in_file.close()
    out_file.close()
    error_file.close()


if __name__ == "__main__":
    main(sys.argv[1:])


