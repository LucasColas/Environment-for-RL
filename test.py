from Q_Learning import create_Q_Table, binning
import sys


Width_chunk, Height_chunk = binning((600,600),20)


Q_Table = create_Q_Table(Width_chunk, Height_chunk)
print(Q_Table)
print("len : ", len(Q_Table))
print(sys.getsizeof(object))
