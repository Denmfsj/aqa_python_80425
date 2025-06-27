import requests

# curl 'https://lms.ithillel.ua/assets/icon/bug.svg' \
#   -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:139.0) Gecko/20100101 Firefox/139.0' \
#   -H 'Accept: image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5' \
#   -H 'Accept-Language: en-US,en;q=0.5' \
#   -H 'Accept-Encoding: gzip, deflate, br, zstd' \
#   -H 'Referer: https://lms.ithillel.ua/groups/6798d97ebcb884d43b014c4d/lessons/6798d97ebcb884d43b014c70?article_id=6744cc9691d73f851fa73900' \
#   -H 'Sec-Fetch-Dest: image' \
#   -H 'Sec-Fetch-Mode: no-cors' \
#   -H 'Sec-Fetch-Site: same-origin' \
#   -H 'Connection: keep-alive' \
#   -H 'Cookie: h_uuid=15e2badb-e358-4b85-a5c4-91e0a5aa23c5; _ga_18JX6GS2RW=GS2.1.s1751040524$o106$g1$t1751043942$j60$l0$h0; _ga=GA1.1.1228211152.1725566841; device-source=https://blog.ithillel.ua/videos/positive-and-negative-aspects-of-automation-video; device-referrer=; ph_phc_MCowB0Klil8CGSp1uP8dgvHGMYLwBN9G3FZ2MMwgH2d_posthog=%7B%22distinct_id%22%3A%220191c3cc-5cff-756f-a8a1-0812a541bf14%22%2C%22%24sesid%22%3A%5B1726503510288%2C%220191fba0-968d-7c08-9ab2-e59182ac7d9f%22%2C1726503491213%5D%2C%22%24epp%22%3Atrue%7D; h_consentMode=%7B%22functionality_storage%22%3A%22granted%22%2C%22security_storage%22%3A%22granted%22%2C%22ad_storage%22%3A%22denied%22%2C%22ad_user_data%22%3A%22denied%22%2C%22analytics_storage%22%3A%22denied%22%2C%22personalization_storage%22%3A%22denied%22%2C%22ad_personalization%22%3A%22denied%22%7D; _clck=1yxbj1e%7C2%7Cfr3%7C0%7C1743; token=s%3AxorsJkFGez7TqTH4uC4KYIK_U4jfvwGJ.AZpwbOSuA0qUnHItDg97%2B8iYu3Voo5iv7xUvEd%2FGZrQ; i18next_lng=uk'


# rs = requests.get(url='https://lms.ithillel.ua/assets/icon/bug.svg',
#              headers={
#                  'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:139.0) Gecko/20100101 Firefox/139.0',
#                  'Accept': 'image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5',
#                  'Accept-Language': 'en-US,en;q=0.5',
#                  'Accept-Encoding': 'gzip, deflate, br, zstd',
#                  'Referer': 'https://lms.ithillel.ua/groups/6798d97ebcb884d43b014c4d/lessons/6798d97ebcb884d43b014c70?article_id=6744cc9691d73f851fa73900',
#                  'Sec-Fetch-Dest': 'image',
#                  'Cookie': 'h_uuid=15e2badb-e358-4b85-a5c4-91e0a5aa23c5; _ga_18JX6GS2RW=GS2.1.s1751040524$o106$g1$t1751043942$j60$l0$h0; _ga=GA1.1.1228211152.1725566841; device-source=https://blog.ithillel.ua/videos/positive-and-negative-aspects-of-automation-video; device-referrer=; ph_phc_MCowB0Klil8CGSp1uP8dgvHGMYLwBN9G3FZ2MMwgH2d_posthog=%7B%22distinct_id%22%3A%220191c3cc-5cff-756f-a8a1-0812a541bf14%22%2C%22%24sesid%22%3A%5B1726503510288%2C%220191fba0-968d-7c08-9ab2-e59182ac7d9f%22%2C1726503491213%5D%2C%22%24epp%22%3Atrue%7D; h_consentMode=%7B%22functionality_storage%22%3A%22granted%22%2C%22security_storage%22%3A%22granted%22%2C%22ad_storage%22%3A%22denied%22%2C%22ad_user_data%22%3A%22denied%22%2C%22analytics_storage%22%3A%22denied%22%2C%22personalization_storage%22%3A%22denied%22%2C%22ad_personalization%22%3A%22denied%22%7D; _clck=1yxbj1e%7C2%7Cfr3%7C0%7C1743; token=s%3AxorsJkFGez7TqTH4uC4KYIK_U4jfvwGJ.AZpwbOSuA0qUnHItDg97%2B8iYu3Voo5iv7xUvEd%2FGZrQ; i18next_lng=uk',
#              })
#
#
# with open('bug.qweqwe', 'wb') as f:
#     f.write(rs.content)
#

import json

response_json = requests.get(url='https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos',
             params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}).json()

print(json.dumps(response_json, indent=4))