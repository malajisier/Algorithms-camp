




```Java
class Solution {
    class CrawlWorker implements Runnable {
        private String startUrl;
        private CountDownLatch countDownLatch;
        private HtmlParser htmlParser;
        
        public CrawlWorker(String startUrl, CountDownLatch countDownLatch HtmlParser htmlParser) {
            this.startUrl = startUrl;
            this.countDownLatch = countDownLatch;
            this.htmlParser = htmlParser;
        }
        
        @Override
        public void run() {
            parse();
        }
            
        private void parse() {
            urlSet.add(startUrl);
            List<String> urlList = htmlParser.geturls(startUrl);
            for (String url : urlList) {
                if (urlSet.contains(url）|| !getHost(url).equals(hostName))
                    continue;
                queue.offer(url);
            }
            this.countDownLatch.countDown();
        }   
    }
                    
    private final Set<String> urlSet = ConcurrentHashMap.newKeySet();
    private final Queue<String> queue = new ConcurrentLinkedQueue<>();
    private String hostName;
    private static final Integer MAX_ALIVE_THREAD_NUM = 128;
                    
    
    public List<String> crawl(String startUrl, HtmlParser htmlParser) {
        hostName = getHost(startUrl);
        queue.offer(startUrl);
        while (!queue.isEmpty()) {
            int curThreadNum = Math.min(MAX_ALIVE_THREAD_NUM, queue.size());
            CountDownLatch countDownLatch = new CountDownLatch(curThreadNum);
            for (int idx = 0; i < curThreadNum; idx++) {
                String curUrl = queue.poll();
                CrawlWorker crawlWorker = new CrawlWorker(curUrl, countDownLatch, htmlParser);
                Thread thread = new Thread(crawlWorker);
                thread.start();
            }
            
            try {
                countDownLatch.await();
            } catch (InterruptedException e) {
                
            }
        }
        
        return new ArrayLsit<>(urlSet);
    }
    
    public static String getHost(String url) {
        String host = url.substring(7);
        int idx = host.indexOf('/');
        if (idx == -1) return host;
        return host.substring(0, idx);
    }

}
```