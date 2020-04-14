import pandas as pd
import numpy as np
def mean_daily_features(Data):
    ind = 0
    cols = ['SubjID','Duration_Mean','Duration_Median','Wear Fraction','NewBrace']
    Features = pd.DataFrame(data=[],columns=cols)

    for newbrace in Data.NewBrace.unique():
        for s in Data.SubjID.unique():
            d = Data[(Data.SubjID==s)&(Data.NewBrace==newbrace)]
            meandur = d['Duration'].mean()
            mediandur = d['Duration'].median()
            wearfrac = d['Wear Frac'].mean()
            sixmwt = np.mean(d['6mwt'])
            tenmwt = np.mean(d['10mwt_ss'])
            cadence = np.nanmean(d['Cadence'])
            #         UsageFrac = np.sum(d['Wear Frac']*d['Duration'])/np.sum(d['Duration'])
            stepsHr = np.nanmean(d['Steps per Hour'])
            age = np.unique(d['Age'])
            BaselineYrs = np.unique(d['BaselineYrs'])

            #daily averages
            dailydur = []; dailysteps = []; dailycadence = []
            for dates in d['Date']:
                dailydur.append(d.loc[d['Date']==dates,'Duration'].sum()) #daily time
                dailysteps.append(d.loc[d['Date']==dates,'Steps'].sum()) #total daily steps

            meddailydur = np.median(dailydur)
            meandailysteps = np.mean(dailysteps)

            Features_ = pd.DataFrame({cols[0]:s, cols[1]:meandur, cols[2]:mediandur, cols[3]:wearfrac,
                                     cols[4]:newbrace, '6mwt':sixmwt, '10mwt_ss':tenmwt, 'Steps':meandailysteps,
                                     'Cadence':cadence, 'Daily Duration':meddailydur, 'Age':age,
                                     'BaselineYrs':BaselineYrs},index=[ind])
            Features = pd.concat([Features,Features_])
            ind+=1

    return Features
