====================
qtmodern6
====================

.. image:: https://img.shields.io/pypi/v/qtmodern6.svg
    :target: https://pypi.python.org/pypi/qtmodern6
    :alt: PyPI Version

``qtmodern6`` 是在``gmarull/qtmodern``项目基础上修改而来的。  
查看原项目请点击：<https://github.com/gmarull/qtmodern>  

原项目只能支持``PyQt``、``PySide2``，且已经停止维护。git上也没能找到类似的项目。
因此就考虑修改原项目以适配``PySide6``。  


主题界面如下图（可能稍有不同）：  

.. image:: examples/mainwindow.png
    :width: 450px
    :align: center
    :alt: Example

基本用法和原来一样。   

安装（python版本>=3.9）：
-----

    pip install qtmodern6

如何使用：
--------

    import qtmodern6.styles
    import qtmodern6.windows

    ...

    app = QApplication()
    win = YourWindow()

    qtmodern6.styles.dark(app)
    mw = qtmodern6.windows.ModernWindow(win)
    mw.show()

    ...

