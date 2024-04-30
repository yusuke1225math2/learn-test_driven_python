import pytest
import tasks
from tasks import Task

def test_add_returns_valid_id(tasks_db):
    """tasks.add(<valid task>) should return an integer"""
    # tasks_dbが初期化済みであるとすれば
    # 新しいタスクが追加されたときに
    # 返されるtask_idはint型
    new_task = Task('do something')
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)

def test_add_increases_count(db_with_3_tasks):
    """フィクスチャでDBにデータ追加した際のtasks.count()の挙動を確認"""
    tasks.add(Task('throw a party'))
    assert tasks.count() == 4
