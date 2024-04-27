import pytest
import tasks
from tasks import Task

@pytest.fixture()
def tasks_db(tmpdir): # tmpdirはディレクトリを表すオブジェクト
    """Connect to db before tests, disconnect after."""
    # セットアップ：dbへの接続を開始
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield # ここでテストを実行
    # ティアダウン：dbへの接続を終了
    tasks.stop_tasks_db()
