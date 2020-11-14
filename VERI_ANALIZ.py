
import seaborn as sns
import pandas as pd
from pandas.api.types import CategoricalDtype
dıamods = sns.load_dataset("diamonds")
df = dıamods.copy()
df.head()

sns.distplot(df.price, bins= 20,kde= False);
(sns
 .FacetGrid(df,
          hue = "cut",
           height = 5,
          xlim = (0,10000))
 .map(sns.kdeplot, "price", shade= True)
 .add_legend() #cut kategorisinin nilgisini eklemek için kullandık
);

import seaborn as sns 
import pandas as pd
tips = sns.load_dataset("tips")
tp = tips.copy()
tp.describe().T

#SORU HANGİ GÜNLER DAHA FAZLA KAZANIYORUZ hangi ögünde daha cok kazanıyoruz
sns.boxplot( x ="day", y =  "total_bill", hue = "time", data = tp);

sns.catplot( x= "total_bill", y = "day" , kind = "violin", data = tp)
sns.scatterplot(x ="total_bill",y= "tip" , hue= "day", style = "time", data=tp);

import seaborn as sns
iris = sns.load_dataset("iris")
ir = iris.copy()
ir.describe().T

#eger yukarıdai grafiklerde markeers ların şeklini degiştirmke isterek
sns.pairplot(ir, hue= "species", markers = ["o","s","D"]); #markers fonksiyonu ile yapabiliriz. aşagıdaki gibi 
#bu işaretler pair plat fonksiyonun içinde belirtilmiştir.















