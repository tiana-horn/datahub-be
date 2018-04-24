from rest_framework import serializers
from .models import LTDBACS_trts_7016,bgs00,bgs1317

class LTDBACS_trts_7016Serializer (serializers.ModelSerializer):
    class Meta:
        model = LTDBACS_trts_7016
        fields = ('id','pop70','nhwht70','pnhwht70','nhblk70','pnhblk70','asian70','pasian70','haw70','phaw70','hu70','vac70','pvac70','ohu70','pohu70','own70','pown70','rent70','prent70','mhmval70a17','mhmval70','mrent70','mrent70a17','hinc70','hinc70a17','ag25up70','hs70','phs70','col70','pcol70','clf70','unemp70','punemp70','pop80','nhwht80','pnhwht80','nhblk80','pnhblk80','ntv80','pntv80','asian80','pasian80','hisp80','phisp80','haw80','phaw80','hu80','vac80','pvac80','ohu80','pohu80','own80','pown80','rent80','prent80','mhmval80','mhmval80a17','mrent80','mrent80a17','hinc80','hinc80a17','hincw80','hincw80a17','hincb80','hincb80a17','hinch80','hinch80a17','hinca80','hinca80a17','ag25up80','hs80','phs80','col80','pcol80','clf80','unemp80','punemp80','pop90','nhwht90','pnhwht90','nhblk90','pnhblk90','ntv90','pntv90','asian90','pasian90','hisp90','phisp90','haw90','phaw90','hu90','vac90','pvac90','ohu90','pohu90','own90','pown90','rent90','prent90','mhmval90','mhmval90a17','mrent90','mrent90a17','hinc90','hinc90a17','hincw90','hincw90a17','hincb90','hincb90a17','hinch90','hinch90a17','hinca90','hinca90a17','ag25up90','hs90','phs90','col90','pcol90','clf90','unemp90','punemp90','pop00','nhwht00','pnhwht00','nhblk00','pnhblk00','ntv00','pntv00','asian00','pasian00','hisp00','phisp00','haw00','phaw00','hu00','vac00','pvac00','ohu00','pohu00','own00','pown00','rent00','prent00','mhmval00','mhmval00a17','mrent00','mrent00a17','hinc00','hinc00a17','hincw00','hincw00a17','hincb00','hincb00a17','hinch00','hinch00a17','hinca00','hinca00a17','meansp9800','minsp9800','maxsp9800','mediansp9800','totsp9800','nums9800','meansp9800a17','minsp9800a17','maxsp9800a17','mediansp9800a17','totsp9800a17','pir9800','ag25up00','hs00','phs00','col00','pcol00','clf00','unemp00','punemp00','pop10','nhwht10','pnhwht10','nhblk10','pnhblk10','ntv10','pntv10','asian10','pasian10','hisp10','phisp10','haw10','phaw10','hu10','vac10','pvac10','ohu10','pohu10','own10','pown10','rent10','prent10','mhmval12','mhmval12a17','mrent12','mrent12a17','hinc12','hinc12a17','hincw12','hincw12a17','hincb12','hincb12a17','hinch12','hinch12a17','hinca12','hinca12a17','meansp0709','minsp0709','maxsp0709','mediansp0709','totsp0709','nums0709','meansp0709a17','minsp0709a17','maxsp0709a17','mediansp0709a17','totsp0709a17','pir0712','ag25up12','hs12','phs12','col12','pcol12','clf12','unemp12','punemp12','pop16','nhwht16','pnhwht16','nhblk16','pnhblk16','ntv16','pntv16','asian16','pasian16','haw16','phaw16','oth16','poth16','twomr16','ptwomr16','hisp16','phisp16','pcnhwht0016','pcnhblk0016','pcasian0016','pchisp0016','hu16','ohu16','pohu16','vac16','pvac16','own16','pown16','rent16','prent16','mhmval16','mrent16','mhmval16a17','mrent16a17','hinc16','hinc16a17','hincw16','hincw16a17','hincb16','hincb16a17','hincn16','hincn16a17','hinca16','hinca16a17','hincp16','hincp16a17','hinco16','hinco16a17','hincm16','hincm16a17','hinch16','hinch16a17','meansp1517','minsp1517','maxsp1517','mediansp1517','totsp1517','nums1517','meansp1517a17','minsp1517a17','maxsp1517a17','mediansp1517a17','totsp1517a17','pir1517','ag25up16','colm16','colf16','col16','pcol16')

class bgs00Serializer (serializers.ModelSerializer):
    class Meta:
        model = bgs00
        fields = ('id','meansp9800','meansp9800a17','minsp9800','minsp9800a17','maxsp9800','maxsp9800a17','mediansp9800','mediansp9800a17','totsp9800','totsp9800a17','nums9800','mhi99','mhi99a17','pir9800','mgr_phi99','mmoc_phi99','pop00','ptwhnl00','ptblknl00','ptnanl00','ptasnl00','ptpanl00','ptothnl00','pt2mnl00','ptlat00','mean_sfno2001','tot_sfno2001','num_sfno2001','mean_sfoo2001','tot_sfoo2001','num_sfoo2001','prc_sfno2001',)

class bgs1317Serializer (serializers.ModelSerializer):
    class Meta:
        model = bgs1317
        fields = ('id','meansp1314','meansp1314a17','minsp1314','minsp1314a17','maxsp1314','maxsp1314a17','mediansp1314','mediansp1314a17','totsp1314','totsp1314a17','nums1314','mhi1314','mhi1314a17','pir1314','mean_sfno100517','tot_sfno100517','num_sfno100517','mean_sfoo100517','tot_sfoo100517','num_sfoo100517','prc_sfno100517','pop13','pop14','ptwhnl13','ptwhnl14','ptblknl13','ptblknl14','ptasnl13','ptasnl14','ptothnl13','ptothnl14','ptlat13','ptlat14','meansp1517','meansp1517a17','minsp1517','minsp1517a17','maxsp1517','maxsp1517a17','mediansp1517','mediansp1517a17','totsp1517','totsp1517a17','nums1517','mhi16','mhi16a17','pir1517','mgr_phi16','mmoc_phi16','mean_sfno011818','tot_sfno011818','num_sfno011818','mean_sfoo011818','tot_sfoo011818','num_sfoo011818','prc_sfno011818','pop16','ptwhnl16','ptblknl16','ptnanl16','ptasnl16','ptpanl16','ptothnl16','pt2mnl16','ptlat16',)
