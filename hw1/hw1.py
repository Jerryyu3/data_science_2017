import sys
import ssl
import matplotlib.pyplot as plt
import urllib


def bar_line_plot(datas, class_name, keys, if_bar):

    fig, ax = plt.subplots()
    men = []; women = []; total = []
    x = range(len(datas))
    
    for data in datas:
        men.append(data[1])
        women.append(data[3])
        total.append((data[0]*data[1]+data[2]*data[3])/(data[0]+data[2]))

    if(if_bar):
        rects1 = ax.bar(x, men, 0.15, color='b')
        rects2 = ax.bar([element + 0.15 for element in x], women, 0.15, color='r')
        rects3 = ax.bar([element + 0.3 for element in x], total, 0.15, color='y')
        ax.set_xticks([element + 0.1 for element in x])

    else:
        ax.plot(x, men, label = 'Male', color='b', marker='x')
        ax.plot(x, women, label = 'Female', color='r', marker='o')
        ax.plot(x, total, label = 'Total', color='y', marker='*')
        ax.set_xticks(x)

    ax.set_title('Smoking Percentage vs ' + class_name)
    ax.set_ylabel('Smoking Percentage (%)')
    ax.set_xticklabels(keys)
    ax.set_xlabel(class_name)

    def autolabel_bar(rects):
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.02*height, '%.1f' % float(height), ha='center', va='bottom')
    if(if_bar):
        autolabel_bar(rects1); autolabel_bar(rects2); autolabel_bar(rects3); 
        ax.legend((rects1[0], rects2[0], rects3[0]), ('Male', 'Female', 'Total'))
    else:
        ax.legend()
        plt.ylim(ymin=0);
        for i in range(len(datas)): 
            plt.text(x[i], men[i]*1.02, '%.1f' % float(men[i]), ha='center', va='bottom')
            plt.text(x[i], women[i]*1.02, '%.1f' % float(women[i]), ha='center', va='bottom')
            plt.text(x[i], total[i]*1.02, '%.1f' % float(total[i]), ha='center', va='bottom')

    plt.show()

def pie_plot(datas, class_name, keys):
    fig, ax = plt.subplots()
    population = dict()
    x = range(len(datas))
    total = 0
    
    for i in x:
        population[keys[i]] = datas[i][0]*datas[i][1]+datas[i][2]*datas[i][3]
        total += population[keys[i]]

    labels = []; proportion = []
    if(len(datas)==3): colors = ['yellowgreen', 'gold', 'lightskyblue']
    else: colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'red']

    for key in population.keys():
        labels.append(key)
        proportion.append(float(population[key])/float(total))

    plt.pie(proportion, labels=labels, colors=colors, autopct='%.1f%%', shadow=False, startangle=0)

    ax.set_title('Proportion of different ' + class_name + ' in smoking population')
    ax.axis('equal')
    #ax.legend()

    plt.show()

if __name__ == '__main__':
    scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    response = urllib.request.urlopen('https://ceiba.ntu.edu.tw/course/481ea4/hw1_data.csv', context=scontext)
    sentences = response.readlines()

    class_data = dict(); i = 0;
    for sentence in sentences:
        if(i==0): 
            i+=1; continue
        sentence = sentence.decode()
        words = sentence.split(',')
        if words[1]!='':
            class_data[words[0]] = [float(words[1]), float(words[2]), float(words[3]), float(words[4])]
    
    for i in range(len(sys.argv)-1):
        if(sys.argv[i+1]=="-Ab"):
            datas = [class_data['20000 and below']]; datas.append(class_data['20001-40000']); datas.append(class_data['40001 and above'])
            bar_line_plot(datas, 'Average monthly income', ['20000 and below', '20001-40000', '40001 and above'], True)

        elif(sys.argv[i+1]=="-Eb"):
            datas = [class_data['elementary school and below']]; datas.append(class_data['junior high']); datas.append(class_data['senior high'])
            datas.append(class_data['university']); datas.append(class_data['graduate school and above'])
            bar_line_plot(datas, 'Education level', 
                    ['elementary school and below', 'junior high', 'senior high', 'university', 'graduate school and above'], True)
            
        elif(sys.argv[i+1]=="-Wb"):
            datas = [class_data['indoor']]; datas.append(class_data['outdoor']); datas.append(class_data['unemployed'])
            bar_line_plot(datas, 'Working environment', ['indoor', 'outdoor', 'unemployed'], True)

        elif(sys.argv[i+1]=="-Al"):
            datas = [class_data['20000 and below']]; datas.append(class_data['20001-40000']); datas.append(class_data['40001 and above'])
            bar_line_plot(datas, 'Average monthly income', ['20000 and below', '20001-40000', '40001 and above'], False)

        elif(sys.argv[i+1]=="-El"):
            datas = [class_data['elementary school and below']]; datas.append(class_data['junior high']); datas.append(class_data['senior high'])
            datas.append(class_data['university']); datas.append(class_data['graduate school and above'])
            bar_line_plot(datas, 'Education level', 
                    ['elementary school and below', 'junior high', 'senior high', 'university', 'graduate school and above'], False)
            
        elif(sys.argv[i+1]=="-Wl"):
            datas = [class_data['indoor']]; datas.append(class_data['outdoor']); datas.append(class_data['unemployed'])
            bar_line_plot(datas, 'Working environment', ['indoor', 'outdoor', 'unemployed'], False)

        elif(sys.argv[i+1]=="-Ap"):
            datas = [class_data['20000 and below']]; datas.append(class_data['20001-40000']); datas.append(class_data['40001 and above'])
            pie_plot(datas, 'average monthly income', ['20000 and below', '20001-40000', '40001 and above'])

        elif(sys.argv[i+1]=="-Ep"):
            datas = [class_data['elementary school and below']]; datas.append(class_data['junior high']); datas.append(class_data['senior high'])
            datas.append(class_data['university']); datas.append(class_data['graduate school and above'])
            pie_plot(datas, 'education level', 
                    ['elementary school and below', 'junior high', 'senior high', 'university', 'graduate school and above'])
            
        elif(sys.argv[i+1]=="-Wp"):
            datas = [class_data['indoor']]; datas.append(class_data['outdoor']); datas.append(class_data['unemployed'])
            pie_plot(datas, 'working environment', ['indoor', 'outdoor', 'unemployed'])



 
 
