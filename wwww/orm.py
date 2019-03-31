#coding=utf-8
#创建连接池
def create_pool(loop,**kw):
    logging.info('create database connection pool....')
    global __pool  #全局变量__pool存储，缺省编码utf-8
    __pool = yield from aiomysql.create_pool(
        host=kw.get('host','192.168.3.60'),
        port=kw.get('port',3306)
        user=kw['root'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset','utf8'),
        autocommit=kw.get('autocommit',True),
        maxsize-kw.get('maxsize',10),
        minisize=kw.get('minszie',1),
        loop=loop
    )
    