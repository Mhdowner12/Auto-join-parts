from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import SessionPasswordNeededError, PhoneCodeInvalidError, PhoneCodeExpiredError
import time

api_id = 28223920
api_hash = '8f1719b54a50472e94175661d630e367'

phone_number = input("Enter your phone number (e.g., +1234567890): ").strip()

# List of groups to join with '@' prefix
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
    '@InstagramAccountFlipping', '@IGmarketplaces', '@igaccountsmarket', '@InstagramTrade', '@buyandselligpage',
    '@chaolsmarket', '@IGAccounts4Sale', '@flamesmarket', '@bargaining', '@powerhousemarket', '@pendingsfs',
    '@c0smicmeghshsbsj', '@grindingmarket2', '@SFSandmarketCC', '@fragmarket', '@hammermarketplace',
    '@cancelsmarket', '@spread4gains', '@sellingpromos', '@igmarke_t', '@gogsmarket', '@volmarket',
    '@akimart', '@aliencatttmarket', '@alienmarkett', '@alienxmarket', '@angelmarkett', '@aomarket',
    '@arkimart', '@armimoremarket', '@auxamarket', '@beachmarketph', '@bebemarket', '@bertsmarket',
    '@bestttmarket', '@bikmrkt', '@blackavenuee', '@blossommarket', '@bluv', '@bobamarket', '@bpmarkettt',
    '@broccoli5k', '@buysellinstaacc', '@buysellwork', '@catmarketzxc', '@circa1988', '@cloudmarketplaces',
    '@cohmedymarket', '@conceiited', '@cpamgroupp', '@culturemarket', '@cynmarket', '@demonmarkett',
    '@diagonalleymart', '@diamondmarketsfs', '@dimmarket', '@dmark8', '@dreimarket', '@dynamitemarket',
    '@elite_likes', '@empressmarketrj', '@engagementgroups', '@eruditemart', '@eusmarkett', '@exquisemarket',
    '@fazeemarket', '@fihrezmarket', '@folkloremarket', '@galaxyzxcv', '@gbpremsmarket', '@gcpromotionph',
    '@ghostmarkeet', '@goblinmarkett', '@godsmarketplace', '@godzillamarketchat', '@goldenigmarket',
    '@goldenmarketlink', '@gomark3t', '@goodmarkat', '@hachemarket', '@heistmart', '@highlightmarket',
    '@hitmanmarket', '@hogwartsmarket', '@icestory', '@igadminmarket', '@igbuysellm', '@igmediamarket',
    '@igsfsmarket', '@infernomarket', '@instagramaccountmarketplace', '@instamarket08', '@instamarket4u',
    '@instamarketo', '@instawoodi', '@izonemarket', '@jahidmarket', '@jamiessfsmarket', '@kakeguruixxmart',
    '@kamarket', '@karasunomarket', '@kingmarketplace', '@kkmarketmarket', '@kvsmarket', '@kymart',
    '@lacasadepapelmarket', '@lafamiliamarket', '@laspaganmarket', '@lasprimasmercado', '@legitestmarket',
    '@levantemarket', '@lfbuyerseller', '@livetradee', '@lucimarket', '@lukesmart', '@lunaaamarket',
    '@magnumarket', '@majestuosmarket', '@marketandsfs', '@marketave', '@marketbosss', '@marketchatsfs',
    '@marketchris', '@marketext', '@marketgoat', '@marketkingdom', '@marketniburnek', '@marketph',
    '@marketplaced', '@marketsfsg', '@marketsplace', '@marksetplace', '@mercadomarket', '@meteormarket',
    '@miamoremarket', '@milesmart', '@mini_martph', '@moonairemarket', '@moonmarkettt', '@myheroacademiamarket',
    '@mysterymart', '@mythologymarket', '@mythsmarket', '@namelessmarkettt', '@nekomart', '@netifypremiumsupplymarket',
    '@nutflixopenmarket', '@nuttymarket', '@oceans_market'
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
                
