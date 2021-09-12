from Q_Learning import create_Q_Table, binning


Width_chunk, Height_chunk = binning((600,600),20)


Q_Table = create_Q_Table(Width_chunk, Height_chunk)
print(Q_Table)
print(f"len : {Q_Table}")
