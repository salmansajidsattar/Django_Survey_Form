from TemporaryStorage import TemporaryStorageInstance

storage = TemporaryStorageInstance()

xy=storage.upload('E:\Django_Survey_Form\\temp_data\output.pdf')
print(xy)
print(type(xy))