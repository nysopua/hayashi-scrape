import scrape_facebook
import scrape_twitter
import scrape_analytics
import slackweb

slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
slack.notify(text= f'{scrape_facebook.getMembers()}\n{scrape_twitter.getFollowersAndFollowees()}\n{scrape_analytics.getData()}')
