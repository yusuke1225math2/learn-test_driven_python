import pytest
import tasks
from tasks import Task

@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # セットアップ：dbへの接続を開始
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield

    # ティアダウン：dbへの接続を終了
    tasks.stop_tasks_db()

@pytest.mark.skip(reason='misunderstood the API')
def test_unique_id_1():
    """Calling unique_id() twice should return different numbers."""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2

def test_unique_id_2():
    """unique_id() should return an unused id."""
    ids = []
    ids.append(tasks.add(Task('one')))
    ids.append(tasks.add(Task('two')))
    ids.append(tasks.add(Task('three')))
    # 一意なIDを取得
    uid = tasks.unique_id()
    assert uid not in ids