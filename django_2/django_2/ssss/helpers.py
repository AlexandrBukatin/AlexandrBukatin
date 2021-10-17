def include_static_content(content=''):
    return '<a href="/"style="padding-right: 12px;">Home</a>'\
        '<a href="/news"style="padding-right: 12px;">News</a>'\
        '<a href="/fact"style="padding-right: 12px;">Fact</a>'\
        '<a href="/management"style="padding-right: 12px;">Management</a>'\
        '<a href="/contacts"style="padding-right: 12px;">Contacts</a>'\
        '<a href="/history"style="padding-right: 12px;">History</a>'\
        f'{content}'