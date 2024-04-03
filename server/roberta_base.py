from simpletransformers.ner import NERModel,NERArgs
import pandas as pd

df_t = pd.read_csv('../data/train.csv')

labels = df_t["type"].unique().tolist()
args = NERArgs()
args.num_train_epochs = 3
args.learning_rate = 1e-4
args.overwrite_output_dir =True
args.train_batch_size = 32
args.eval_batch_size = 32

model = NERModel('roberta', '../outputs/checkpoint-189-epoch-3',labels=labels,args=args, use_cuda=False)
def modifyPrompt(p = ""):
  p = p.replace("'", " ' ")
  p = p.replace("\"", " ' ")
  return p

def makePrediction(prompt):
    prediction, model_output = model.predict([modifyPrompt(prompt)])

    pred = prediction[0]
    idx = 0
    n = len(pred)
    for c in pred:
        x = list(c.values())[0]
        y = list(c.keys())[0]
    
        if idx > 0 and idx < n-1:
            l = list(pred[idx-1].values())[0]
            r = list(pred[idx+1].values())[0]
            if  x == "O" and l != "O" and r != "O" and l.split("-")[1] == "CNT" and r.split("-")[1] == "CNT":
                pred[idx][y] = "I-CNT"
    
        idx += 1
    
    out = []
    for p in pred:
      x = list(p.values())[0]
      y = list(p.keys())[0]
    
      if (x != "O"):
        a = x.split("-")
        match a[1]:
          case "AT" | "RT" | "CT":
            if (a[0] == "B"):
                dict = {}
                dict["TYPE"] = a[1]
                dict["CNT"] = ""
                out.append(dict)
          case "CNT":
            if (len(out) == 0):
              print("type is missing!")
            else:
              if (out[-1]["CNT"] == ""):
                out[-1]["CNT"] = y
              else:
                out[-1]["CNT"] += " " + y
          case _:
            pass

    return out