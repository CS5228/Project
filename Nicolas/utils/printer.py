import keras
from keras.utils.vis_utils import plot_model
from matplotlib import pyplot as plt

class nn_printer:
   
    def __init__(self,model):
        self.model = model 
    
    def model_to_png(self,filename,bool_show_shapes=True, bool_show_layer_names=True):
        plot_model(self.model, to_file='{}.png'.format(filename),show_shapes=bool_show_shapes, show_layer_names=bool_show_layer_names)
        
    def history_to_graph_acc(self,history,exportPNG=False,path_to_export=None):
        plt.figure()
        plt.plot(history['accuracy'], marker='o', color="blue", alpha=0.3)
        plt.plot(history['val_accuracy'], marker='o', color="orange", alpha=0.3)
        plt.title('model accuracy')
        plt.ylabel('accuracy')
        plt.xlabel('epoch')
        plt.legend(['train', 'val'], loc='upper left')
        
        
        if exportPNG:
            plt.savefig(path_to_export,bbox_inches="tight")
        
 
        plt.show()
    
    def history_to_graph_loss(self,history,exportPNG=False,path_to_export=None):
        plt.figure()
        plt.plot(history['loss'], marker='o', color="blue", alpha=0.3)
        plt.plot(history['val_loss'], marker='o', color="orange", alpha=0.3)
        plt.title('model loss')
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.legend(['train', 'val'], loc='upper left')
        
        
        if exportPNG:
            plt.savefig(path_to_export,bbox_inches="tight")
            
        plt.show()
        
        

