from collections import defaultdict
import json
import glob
import time
import sys
from multiprocessing import Process, Pool

def findFiles(path):
    return glob.glob(path)

def read_json(path):
    dict = defaultdict(lambda: defaultdict)
    start_time = time.time()
    counter = 0
    all_path = findFiles(path+'/*.json')
    all_num = len(all_path)

    # def to_dict(path):
    #     openTrainData = open(filename);
    #     trainData = json.load(openTrainData);
    #     openTrainData.close();
    #     dict[trainData["id"]] = trainData
    #     counter+=1
    #     if (time.time()-start_time > 10):
    #         start_time = time.time()
    #         print(str(counter) + " .json files have be readed in " + path + ', ' + str(all_num-counter) + ' remains')
    #
    # pool = Pool(processes=4)  # start 4 worker processes
    # result = pool.map(to_dict, all_path)


    for filename in all_path:
        openTrainData = open(filename);
        trainData = json.load(openTrainData);
        dict[trainData["id"]]=trainData
        counter+=1
        if (time.time()-start_time > 10):
            start_time = time.time()
            print(str(counter) + " .json files have be readed in " + path + ', ' + str(all_num-counter) + ' remains')
    return dict




if __name__ == "__main__":
    name = sys.argv[1]
    dict = read_json('../project-data/' + name + '.data-object')
    with open( name + ".json", 'w' ) as outfile:
        json.dump(dict, outfile)
    print('Hello World')
