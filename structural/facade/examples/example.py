from ..pattern.base import (
    BaseDBManager,
    BaseFileManagerFacade,
    BaseFileStorageManager,
    BaseFileSystemManager,
)

mok_database = dict()
mok_file_storage = dict()
mok_file_system = dict()

test_db_manager = BaseDBManager(mok_database=mok_database)
test_st_manager = BaseFileStorageManager(mok_file_storage=mok_file_storage)
test_fs_manager = BaseFileSystemManager(mok_file_system=mok_file_system)
test_file_manager = BaseFileManagerFacade(
    db_manager=test_db_manager,
    st_manager=test_st_manager,
    fs_manager=test_fs_manager,
)
