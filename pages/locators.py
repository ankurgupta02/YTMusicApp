class Player_Locators:
    PLAYLIST_QUEUE = "//ytmusic-player-queue//*[@id='contents']"
    PLAYLIST_QUEUE_ALLVIDEOS_TITLES = "//*[@id='contents']//yt-formatted-string[contains(@class, 'song-title')]"

class Home_Locators:
    SHELF_XPATH = "//ytmusic-carousel-shelf-renderer[1]//*[@id='items']"
    SHELF_ALLITEMS_XPATH = "//*[@id='items']/ytmusic-responsive-list-item-renderer"
    SHELF_SUBMENUITEM_XPATH = "//yt-formatted-string[normalize-space()='{item}']"  # dynamic xpath can be used for item and submenuitem

    DIALOGBOX_SIGNIN_BUTTON_XPATH = "//*[@id='contentWrapper']//yt-button-shape/button"
    LIKE_BUTTON = "//*[@id='button-shape-like']"
    DISLIKE_BUTTON = "//*[@id='button-shape-dislike']"
    CONTEXTUAL_MENU_BUTTON = "//*[@id='button-shape']"

    PREVIOUS_BUTTON_ON_SHELF = "//ytmusic-carousel-shelf-renderer[1]//*[@id='previous-items-button']"
    NEXT_BUTTON_ON_SHELF = "//ytmusic-carousel-shelf-renderer[1]//*[@id='next-items-button']"
    PLAYALL_BUTTON = "//ytmusic-carousel-shelf-renderer[1]//*[@id='more-content-button']"

    SHELF_ALLVIDEOS_TITLES = "//ytmusic-carousel-shelf-renderer[1]//*[@id='items']//yt-formatted-string[contains(@class, 'title')]"

class Login_Locator:
    SIGN_IN_BUTTON = "//a[normalize-space()='Sign in']"
    EMAIL_ID = "//input[@id='identifierId']"
    NEXT_BUTTON = "//span[normalize-space()='Next']"
    PASSWORD = "//input[@name='Passwd']"
    NOT_NOW_BUTTON = "//span[normalize-space()='Not now']"
    AVATAR_BUTTON = "//*[@id='button']//img[@id='img']"
    SIGN_OUT_BUTTON = "//yt-formatted-string[normalize-space()='Sign out']"

    SIGN_IN_TEXT_LEFT_GUIDE = "//*[@id='guide-renderer']//yt-formatted-string[contains(text(),'Sign in to create & share playlists')]"
    LEFT_GUIDE_BUTTON = "//*[@id='left-content']//yt-icon[@id='guide-icon']"

    SIGN_IN_BUTTON_WHEN_LEFTGUIDE_EXPANDED = "//*[@id='sign-in-button']//*[@class='yt-spec-touch-feedback-shape__fill']"
    SIGN_IN_BUTTON_WHEN_LEFTGUIDE_COLLAPSED = "//*[@id='mini-guide']//ytmusic-guide-signin-promo-renderer[@class='style-scope ytmusic-guide-renderer']"
