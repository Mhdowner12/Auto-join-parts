from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import SessionPasswordNeededError, PhoneCodeInvalidError, PhoneCodeExpiredError
import time

api_id = 28223920
api_hash = '8f1719b54a50472e94175661d630e367'

phone_number = input("Enter your phone number (e.g., +1234567890): ").strip()

# Updated list of groups with '@' prefix
group_list = [
    '@talamarkettt', '@tays56', '@teampayamanmarket', '@teiemart', '@telehub2', '@telemarketph',
    '@telemartph', '@telepromobuyselltrade', '@TeleStoreOGChat', '@teleworldmarket', '@terramarket',
    '@tgmegamart', '@tgonlinemarket', '@theblackmarket', '@thebloommartph', '@theboysmarketplace',
    '@thecloutmarket', '@TheDMarket', '@theelfantasma', '@TheFinalMarket', '@TheGalaxyMarket',
    '@Thejunglemarket', '@thekentmart', '@themobilemarket', '@thenightmarket', '@thepeachymart',
    '@ThePlugMarket', '@thepugmarket', '@theredmarket', '@ThrillsMarket', '@titanmarket',
    '@tjsmarketplacepublic', '@TMBusinessSocialMediaSellGroup', '@tmbusinesssocialmediasellgroup',
    '@TMGMarket', '@topmarts', '@trufflesfs', '@TrustedMarket', '@twiceujjangmarket', '@umbrellamarket',
    '@undergroundmarket1620', '@unholymarket', '@universalmarkettt', '@urbanmarketph', '@versacemarket',
    '@viralsmarket', '@virgomarketplace', '@vntrmarket', '@w0rldmarket', '@Waitermarket', '@wasgmarket',
    '@wbmarketingmarket', '@windsales', '@wobblezmarket', '@wolf_market20', '@wysmarketingchat',
    '@xiomarkett', '@yamerokudasaiii', '@ycmmarket', '@yourshopfindmarket', '@ziamarket', '@eueysstyle',
    '@everyonecanchat', '@explosiveness', '@ezmartttt', '@ezplaza', '@faerymart', '@fashionablzpowerlikes',
    '@fcftoken1', '@fcftokenan', '@foodiesdx30likesonly', '@forexbiglotz', '@forextrading444', '@forhome3d',
    '@fraggingshop', '@fraudalert21', '@bluve', '@sanemarket', '@PlMPS', '@royalmarkets', '@GodsMarket',
    '@NsmIGGroup', '@marketinfinity', '@Mediasalez', '@ProsperMarket', '@Epmarket', '@marketlmfao',
    '@CriticalMarket', '@socialsmarket', '@SickwebMarket', '@socialmediamarkett', '@socialgrowthmarket',
    '@ghostmarket', '@Betmarkett', '@InstagramMarket', '@makeemoney', '@monstermarket', '@lucifermarket',
    '@millionairemarket', '@successed', '@Gosomarket', '@billboardmarket', '@socialsprint', '@MMMarket',
    '@DISCOVERmarket', '@instaempiremarket', '@generalmarketplace', '@sfsmarketbuyandsell', '@socialtoolsmarket',
    '@instagramIGIG', '@memescommumity', '@TakeoffMarket', '@buyandsellmarketplace', '@marketplace_ig',
    '@InstagramsMarket', '@Instamarketplace', '@admitmarket', '@xploreshop', '@securemarket', '@eSocialMarket',
    '@Gainmedia', '@themainmarket', '@boostmarket', '@Futureboost', '@apocmarket', '@SNTADS', '@adsment',
    '@shanksmarket', '@socialgrowthmarkett', '@IGAccounts', '@MediaMarkett', '@facemarket', '@ExclusiveMarket',
    '@TheRedMarket', '@a1sell', '@BlackMarkets', '@newmarket01', '@ViralMarket', '@Depositsonlymarket',
    '@EvolveMarket', '@eliteinstamarket', '@BoostFameMarket', '@almarketgroup', '@bmwmarket', '@OGUsernames',
    '@Nooses', '@safetymarkett', '@onlineads_markets', '@instaaccountsell', '@igbuysellzz',
    '@InstagramAccountFlipping', '@IGmarketplaces', '@XMARKETPLACE', '@igaccountsmarket', '@InstagramTrade',
    '@buyandselligpage', '@chaolsmarket', '@IGAccounts4Sal'
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
                
                # Sleep for 15 minutes after every 5 groups
                if (i + 1) % 5 == 0:
                    print("Sleeping for 15 minutes...")
                    time.sleep(900)  # 900 seconds = 15 minutes
                
            except PhoneCodeInvalidError:
                print(f"Invalid code for {group}")
            except PhoneCodeExpiredError:
                print(f"Code expired for {group}")
            except Exception as e:
                print(f"Failed to join {group}: {e}")
                
    except Exception as e:
        print(f"An error occurred: {e}")
