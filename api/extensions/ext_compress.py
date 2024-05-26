from flask import Flask


def init_app(app: Flask):
    if app.config.get('API_COMPRESSION_ENABLED', False):
        from flask_compress import Compress

        # 设置压缩的MIME类型
        app.config['COMPRESS_MIMETYPES'] = [
            'application/json',
            'image/svg+xml',
            'text/html',
        ]

        # 启用http内容压缩，以减少传输的数据量，从而提高网站的性能
        compress = Compress()
        compress.init_app(app)

