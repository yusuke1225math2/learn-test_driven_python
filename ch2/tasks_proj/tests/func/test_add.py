import pytest
import tasks
from tasks import Task

def test_add_returns_valid_id():
    """tasks.add(<valid task>) should return an integer"""
    # tasks_dbが初期化済みであるとすれば
    # 新しいタスクが追加されたときに
    # 返されるtask_idはint型
    new_task = Task('do something')
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)

@pytest.mark.smoke
def test_added_task_has_id_set():
    """ Make sure the task_id field is set by tasks.add()."""
    # tasks_dbが初期化済みで新しいタスクが追加されるとすれば
    new_task = Task('sit in chair', owner='me', done=True)
    task_id = tasks.add(new_task)

    # タスクが取得されたときに
    task_from_db = tasks.get(task_id)

    # task_idはidフィールドと一致する
    assert task_from_db.id == task_id

@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # セットアップ：dbへの接続を開始
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield

    # ティアダウン：dbへの接続を終了
    tasks.stop_tasks_db()
