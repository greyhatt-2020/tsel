import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))