from datatools.dataiter import DirHandler, LMDBHandler
from datatools.mechanic.video.track import track_dataiter

# SRCPATH = '/unsullied/sharefs/liyang/facerec-raw-data/hankou-subway/'
SRCPATH = '/unsullied/sharefs/wangfeihong/facerec/zip/Albina/'

DISTPATH = '/unsullied/sharefs/wangfeihong/facerec/hankou/track3'

dr = DirHandler.open(SRCPATH, 'rb',
    absolute_path=True,
    include_subdirs=True,
    patterns=['*.mp4'],
    )


track_dataiter(dr, DISTPATH,
    track_conf='tracker.xlarge.v3.conf',
    replica=4,
    device='cpu0'
    #use_rrun=False, 
    #device='gpu0'    #verbose=True,
    #Handler=LMDBHandler,
    )
