from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import SessionPasswordNeededError, PhoneCodeInvalidError, PhoneCodeExpiredError
import time

api_id = 28223920
api_hash = '8f1719b54a50472e94175661d630e367'

phone_number = input("Enter your phone number (e.g., +1234567890): ").strip()

# List of groups to join with '@' prefix
group_list = [
    '@fihrezmarket', '@folkloremarket', '@freakymega', '@futureboost', '@gainmedia', '@galaxyzxcv',
    '@gbpremsmarket', '@gcpromotionph', '@generalmarketplace', '@ghostmarkeet', '@ghostmarket',
    '@goblinmarkett', '@GodsMarket', '@godsmarket', '@godsmarketplace', '@godzillamarketchat',
    '@goldenigmarket', '@goldenmarketlink', '@gomark3t', '@goodmarkat', '@Gosomarket', '@greengains',
    '@grindingmarket', '@grindingsfsmarket', '@groupsharesfs', '@hachemarket', '@hackerschatz',
    '@hammermarketplace', '@heistmart', '@highlightmarket', '@himarket1', '@hitmanmarket',
    '@hogwartsmarket', '@hubofmarkets', '@icestory', '@igadminmarket', '@igbst', '@igbuysellm',
    '@igmarketplaces', '@igmediamarket', '@igsfsmarket', '@imperialmarket', '@infernomarket',
    '@instabossmarket', '@instaempiremarket', '@instagramaccountmarketplace', '@InstagramMarket',
    '@instagrammarket', '@instagrampagesales', '@instagramsmarket', '@instagramventuresmarket',
    '@instamarket08', '@instamarket4u', '@instamarketo', '@instawoodi', '@izonemarket', '@jacesmarket',
    '@jahidmarket', '@jamiessfsmarket', '@kakeguruixxmart', '@kamarket', '@karasunomarket',
    '@kingmarketplace', '@kkmarketmarket', '@kvsmarket', '@kymart', '@lacasadepapelmarket',
    '@lafamiliamarket', '@laspaganmarket', '@lasprimasmercado', '@legitestmarket', '@levantemarket',
    '@lfbuyerseller', '@livetradee', '@lividmarket', '@lookingfor_ph', '@lucifermarket', '@LucifersMarket',
    '@lucimarket', '@lukesmart', '@lunaaamarket', '@magnumarket', '@majestuosmarket', '@makeemoney',
    '@malcominthemiddle', '@marketandsfs', '@marketave', '@marketbosss', '@marketchatsfs', '@marketchris',
    '@marketext', '@marketgoat', '@marketinfinity', '@marketkingdom', '@marketlmfao', '@marketmeme',
    '@marketniburnek', '@marketph', '@marketplaced', '@marketsfsg', '@marketsplace', '@marksetplace',
    '@maroonmarket', '@mediamarkett', '@Mediasalez', '@mercadomarket', '@meteormarket', '@miamoremarket',
    '@milesmart', '@millionairemarket', '@mini_martph', '@MMMarket', '@mmmarket', '@MoneyMartOG',
    '@moneymartog', '@monstermarket', '@moonairemarket', '@moonmarkettt', '@myheroacademiamarket',
    '@mysterymart', '@mythologymarket', '@mythsmarket', '@namelessmarkettt', '@nekomart', '@nestormarket',
    '@netifypremiumsupplymarket', '@NsmIGGroup', '@nsmiggroup', '@nutflixopenmarket', '@nuttymarket',
    '@oceans_market', '@oginstagramm', '@ogmarts', '@ogusernames', '@olympusmarket', '@onepiecemarket',
    '@onyxmarkettt', '@ourigmarket', '@palengke', '@paradisomarket', '@parallelmarket02', '@pawxiemarket',
    '@paxchat', '@paxinstagram', '@percmarts', '@peytxxmarket', '@phmartpremiums', '@phvirtualmarket',
    '@pietersmarket', '@piscesmarket', '@platinummarket', '@plazadeac', '@PlMPS', '@popthatpussyptp',
    '@PowerMarketing', '@premiermarket', '@PremiumMarketplace', '@premiummarketplace', '@premiumsmarketplace',
    '@premiumszxcc', '@premsmania', '@projecttgmarket', '@ProsperMarket', '@psychomarkett', '@pyxismarket',
    '@reconmarket', '@redymarket', '@renevagemarket', '@rfrmarket', '@riosmarket', '@royalmarkets',
    '@rvelvetmarket', '@sandboxmart', '@sanemarket', '@sanemarketing', '@sarisarimarket', '@satiremarketsfs',
    '@sbmarkett', '@scammarketph', '@securemarket', '@serpentmarkett', '@sevendeadlysinsmarket', '@sfs_market',
    '@sfsactivez', '@sfsbabes', '@sfsbuysell', '@sfschats', '@sfsgrinds', '@sfsgroupjoin', '@sfshubs',
    '@sfsmarket2', '@sfsmarket3', '@sfsmarket4', '@sfsmarket5', '@sfsmarket6', '@sfsmarketchat',
    '@sfsmarketing', '@sfsmarkets', '@shanksmarket', '@shoutoutforshoutouts', '@SickwebMarket',
    '@sijangmarket', '@sinserssfs', '@sismark8', '@skylersmarket', '@slappiie', '@slumdrunk',
    '@slxrpsmarket', '@smmarketlounge', '@snapchatgainchat', '@snoflakesfs', '@sntads', '@socialbuyandsell',
    '@SocialCapitalmarket', '@socialgrowthmarket', '@socialmaniaog', '@socialmarket', '@socialmarkets',
    '@socialmediamarkett', '@socialsmarket', '@socialsprint', '@solanamart', '@solastamarketplace',
    '@soleilmarket', '@solmarkett', '@sosanti', '@souruteikamarketx', '@spoktimarket', '@ssgains',
    '@steppagainsrfr', '@stopnshoppe', '@successed', '@supernovamarketplace', '@supremotrade', '@surgemarket',
    '@surgesocialmarket', '@sushisaucemarket'
]

with TelegramClient(phone_number, api_id, api_hash) as client:
    try:
        client.connect()
        
        if not client.is_user_authorized():
            client.send_code_request(phone_number)
            try:
                client.sign_in(phone_number, input('Enter the code: '))
            except SessionPasswordNeededError:
                password = input('Two-factor authentication is enabled. Please enter your password: ')
                client.sign_in(password=password)
                
        for i, group in enumerate(group_list):
            try:
                result = client(JoinChannelRequest(group))
                print(f"Successfully joined {group}")
                
                # Sleep for 13 minutes after every 5 groups
                if (i + 1) % 5 == 0:
                    print("Sleeping for 13 minutes...")
                    time.sleep(780)  # 780 seconds = 13 minutes
                
            except PhoneCodeInvalidError:
                print(f"Invalid code for {group}")
            except PhoneCodeExpiredError:
                print(f"Code expired for {group}")
            except Exception as e:
                print(f"Failed to join {group}: {e}")
                
    except Exception as e:
        print(f"An error occurred: {e}")
