import sys, os, argparse, json, pprint

def main(arguments):

    parser = argparse.ArgumentParser(description="This is my script", formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-f', '--api_dir', help="dir for json files", default="C:\\Users\\will\\Documents\\Visual Studio 2017\\Projects\\winapi-json\\api_by_category")
    parser.add_argument('-s', '--search', help="Search term(s) separated by comma", default="thread")
    parser.add_argument('-c', '--data_type', help='Data to search in argument structure (in_out, type, name, description)', default='description')
    args = parser.parse_args(arguments)

    terms = args.search.split(',')
    api_files = os.listdir(args.api_dir)

    for api_file in api_files:
        open_file = os.path.join(args.api_dir, api_file)
        with open(open_file, 'r') as f:
            data = json.load(f)
            for obj in data:
                for api_args in obj['arguments']:
                    for term in terms:
                        if term in api_args[args.data_type]:
                            print('{}---------------------------------------------------------------'.format(term))
                            print('API: {}\nDescription: {}\n'.format(obj['category'], obj['name'], obj['description']))
                            print('Arguments: {}\nType: {}\nName: {}\nDescription: {}\n'.format(api_args['in_out'], api_args['type'], api_args['name'], api_args['description']))

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
