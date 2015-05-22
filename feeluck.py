# Vivek Keshore
# http://www.spoj.com/problems/FEELUCK/

inputs = int(raw_input())
for inp in xrange(inputs):
    url_data = {}
    max_val = 0
    for i in xrange(10):
        info = raw_input().split()
        url, val = info[0], int(info[1])
        urls = url_data.get(val)
        if not urls:
            url_data[val] = [url]
        else:
            urls.append(url)

        if max_val < val:
            max_val = val
    print 'Case #{}:'.format(inp+1)
    for url in url_data.get(max_val):
        print url
