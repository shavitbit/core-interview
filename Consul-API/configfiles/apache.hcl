service {
    name = "apache"
    tags = ["web"]
    port = 8080

    check {
        id = "apache-8080"
        name = "http health check page on port 8080"
        http = "http://localhost:8080/health.html"
        interval = "10s"
        timeout = "2s"
    }
}