import os
from binary_extractor.platforms.ETH.cfg import EthereumCFG
from binary_extractor.analysis.graph import CFGGraph
from shutil import copyfile


def bytecode_to_cfg(vuln):
    fileList1 = os.listdir(f"./bytecode/{vuln}/")
    fileList = []
    for file_name in fileList1:
        if '.txt' in file_name:
            fileList.append(file_name)

    currentpath = os.getcwd()

    for file_name in fileList:
        f = open(f"./bytecode/{vuln}/" + file_name, 'r')

        # global bytecode_hex
        bytecode_hex = f.read()
        f.close()

        # create the CFG
        cfg = EthereumCFG(bytecode_hex)

        # generic visualization api
        # graph = CFGGraph(cfg)
        # graph.view()

        print(file_name + " is done!")

        os.chdir(currentpath)
        cfgList = os.listdir(f"./binary_cfg_code/{vuln}/")
        cfgList.sort(key=lambda x: int(x[:-4]))

        if (str(file_name)[0:-4] + '.' + 'txt') not in cfgList:
            copyfile('./graph.cfg.gv',
                     f"./binary_cfg_code/{vuln}/" + str(file_name)[0:-4] + '.' + 'txt')
            os.chdir(f"./binary_cfg_code/{vuln}/")
            print(str(file_name)[0:-4])

        os.chdir(currentpath)


if __name__ == '__main__':
    vuln_list = ["delegatecall", "integeroverflow", "reentrancy", "timestamp"]
    for vuln in vuln_list:
        bytecode_to_cfg(vuln)
