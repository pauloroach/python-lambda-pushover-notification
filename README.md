# Python Lambda AWS Pushover Notification
AWS Python Lambda that publishes Pushover Notification

## Configuration
Replace user_key = 'xxxxxxxx' and api_token = 'xxxxxxxxx'

| Parameter | Value                                  |
|-----------|----------------------------------------|
| Runtime   | Python 3.11                            |
| Handler   | `pushover_notification.lambda_handler` |
| Memory    | 128 MiB (only uses ~40)                |
| Timeout   | 5 seconds                              |
