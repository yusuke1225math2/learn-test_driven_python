def test_tmpdir(tmpdir):
    # tmpdirからはpy.path.local型のオブジェクトが返される
    # 関数スコープのフィクスチャなので、関数以外のスコープのフィクスチャならtmpdir_factoryを使う
    # tmpdirにはパス名が既に関連付けられている
    # join()はファイル名を含むようにパスを拡張する
    # ファイルは書き込みじい作成される
    a_file = tmpdir.join('something.txt')

    # ディレクトリを作成できる
    a_sub_dir = tmpdir.mkdir('anything')

    # ディレクトリにファイルを作成できる
    another_file = a_sub_dir.join('something_else.txt')

    # この書き込みにより'something.txt'が作成される
    a_file.write('contents may settle during shipping')

    # この書き込みにより'anything/something_else.txt'が作成される
    another_file.write('something different')

    assert a_file.read() == 'contents may settle during shipping'
    assert another_file.read() == 'something different'

def test_tmpdir_factory(tmpdir_factory):
    # まずディレクトリを作成する
    # a_dirはtmpdirフィクスチャから返されたオブジェクトのように動作する
    a_dir = tmpdir_factory.mktemp('mydir')

    # base_tempはmydirの親ディレクトリ
    # ここではgetbasetemp()を使用する必要はない
    # この関数が利用可能であることの説明のために書いてるだけ
    base_temp = tmpdir_factory.getbasetemp()
    print('base: ', base_temp)

    # このテストの残りの部分は、tmpdirの代わりにa_dirを使っているだけで、test_tmpdirと同じ

    a_file = a_dir.join('something.txt')
    a_sub_dir = a_dir.mkdir('anything')
    another_file = a_sub_dir.join('something_else.txt')

    a_file.write('contents may settle during shipping')
    another_file.write('something different')

    assert a_file.read() == 'contents may settle during shipping'
    assert another_file.read() == 'something different'
