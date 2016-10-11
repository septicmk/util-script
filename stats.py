import matplotlib.pyplot as plt
import numpy as np
import json



def draw_pie_runtime(ready_ticks, polling_ticks, idle_ticks):
    labels = ['Active', 'Polling', 'Idle']
    sizes = [ready_ticks, polling_ticks, idle_ticks]
    colors = ['yellowgreen', 'lightskyblue', 'lightcoral'];
    explode = (0, 0, 0.1)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',shadow=True, startangle=90)
    plt.axis('equal')
    plt.savefig('./profiling/imgs/runtime.eps', dpi=75)
    plt.cla()
    #plt.show();

def draw_pie_rdma_pct(local, rdma):
    labels = ['Local_bytes', 'RDMA_bytes']
    sizes = [local, rdma]
    colors = ['yellowgreen', 'lightskyblue'];
    explode = (0, 0.1)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',shadow=True, startangle=90)
    plt.axis('equal')
    plt.savefig('./profiling/imgs/imgsrdma_pct.eps', dpi=75)
    plt.cla()
    #plt.show();

def draw_plot(rank):
    b ="/store/blade11/test/test_graph500/static/"
    for r in range(rank):
        print "now is at " + str(r) + "/" + str(rank)
        fn = "task_static_rank_" + str(r)
        d_fn = b + fn
        data = np.loadtxt(d_fn)
        x = range(len(data))
        data=data.T
        #with plt.style.context('fivethirtyeight'):
        plt.plot(x, data[2], color='yellow')
        plt.plot(x, data[1], color='green')
        plt.plot(x, data[0], color='red')
        plt.savefig("./profiling/imgs/"+fn+".png", dpi=160)
        plt.cla()

def draw_time_pie(rank):
    b ="/store/blade11/test/test_graph500/stage_time/"
    for r in range(rank):
        print "now is at " + str(r) + "/" + str(rank)
        fn = "stage_tot_" + str(r) + ".data"
        d_fn = b + fn

        data = np.loadtxt(d_fn)
        labels = ['User', 'System', 'Communication', 'Deaggregation', 'Scheduler', 'Findwork']
        colors = ['yellow', 'lightskyblue', 'lightcoral', 'red', 'green', 'violet'];
        pcts = 100.*data/data.sum()
        labels = ['{0} - {1:1.2f}%'.format(i, j) for i,j in zip(labels, pcts)]


        explode = (0, 0, 0, 0, 0, 0)
        patches, texts = plt.pie(data, explode=explode, colors=colors, shadow=True, startangle=90)
         
        patches, labels, dummy = zip(*sorted(zip(patches, labels, data), key=lambda x: x[2], reverse=True) )
        plt.legend(patches, labels, loc='center left', fontsize=14)
        plt.axis('equal')
        #plt.show()
        plt.savefig('./profiling/imgs/pie/' + fn + '.png', dpi=160)
        plt.cla()




if __name__ == "__main__":
    #pwd="/store/blade11/test/test_graph500/grappa/stats.json"
    #pwd="/store/blade11/test/test_gups/grappa/stats.json"
    #data = {}
    #with open(pwd,'r') as f:
        #data = json.load(f)
    #draw_pie_runtime(data["scheduler_ready_thread_ticks"], data["scheduler_polling_thread_ticks"], data["scheduler_idle_thread_ticks"])
    #draw_pie_rdma_pct(data["app_bytes_delivered_locally"], data["rdma_message_bytes"])
    #draw_plot(64)
    draw_time_pie(64);




