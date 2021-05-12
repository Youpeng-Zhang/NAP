import pickle,os,sys,getopt

AAs=['A','T','C','G','S',
     'R','K','Q','E','L',
     'I','Y','V','M','W',
     'D','N','H','F','P']
path=''
input_file=''
output_file=''

def Parameters():
    print('#########################Parameters#########################'+'\n'+
          '-h     show help information'+'\n'+
          '-p     specify the path to the location of the folder "NAP"'+'\n'+
          '-i     specify the input file'+'\n'+
          '-o     specify the output file'+'\n'+
          '############################################################')

try:
    opts,args=getopt.getopt(sys.argv[1:],'h:p:i:o:')
    for parameter,value in opts:
        if parameter in ('-h'):
            Parameters()
            sys.exit(1)
        if parameter in ('-p'):
            path=value
        if parameter in ('-i'):
            input_file=value
        if parameter in ('-o'):
            output_file=value
except getopt.GetoptError:
    Parameters()
    sys.exit(1)

if '' not in [path,input_file,output_file]:
    input = open(path + '/NAP/model_files/model.pkl', 'rb')
    model = pickle.load(input)
    input.close()

    os.system('echo Reading input file ...')
    IDs = []
    list_CDRH1_2_3 = []
    test_x = []
    id = ''
    for line in open(input_file):
        if line[0] == '>':
            id = line[:-1].split('\t')[0]
        if line[0] != '>':
            CDRH1_2_3 = line[:-1].split('\t')
            values = []
            for seq in CDRH1_2_3:
                dipeps = []
                dict_tmp = {}
                for index in range(0, len(seq) - 1):
                    dipep = seq[index:index + 2]
                    if dipep in dict_tmp.keys():
                        dict_tmp[dipep] += 1
                    if dipep not in dict_tmp.keys():
                        dict_tmp[dipep] = 1
                for AA1 in AAs:
                    for AA2 in AAs:
                        dipep = AA1 + AA2
                        if dipep not in dipeps:
                            dipeps.append(dipep)
                            if dipep in dict_tmp.keys():
                                values.append(dict_tmp[dipep] / (len(seq) - 1))
                            if dipep not in dict_tmp.keys():
                                values.append(0)
            test_x.append(values)
            IDs.append(id)
            list_CDRH1_2_3.append(line[:-1])

    os.system('echo Predicting ...')
    scores = model.predict(test_x)
    save_file = open(output_file, 'w')
    os.system('echo Writing to the output file ...')
    save_file.write('#score>0.5 represents neutralizing' + '\n' + 'ID' + '\t' + 'CDRH1' + '\t' + 'CDRH2' + '\t' + 'CDRH3' + '\t' + 'score' + '\t' + 'neutralizing' + '\n')
    index = 0
    for score in scores:
        neutralizing = 'non-neutralizing'
        if float(score) > 0.5:
            neutralizing = 'neutralizing'
        save_file.write(IDs[index] + '\t' + list_CDRH1_2_3[index] + '\t' + '%.3f' % (score) + '\t' + neutralizing + '\n')
        index += 1
    save_file.close()
    os.system('echo Prediction finished!')
else:
    os.system('echo Required parameters are not specified! You can check by parameter -h.')