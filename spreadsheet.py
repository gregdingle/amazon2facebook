try:
    from xml.etree import ElementTree
except ImportError:
    from elementtree import ElementTree
import gdata.spreadsheet.service
import gdata.service
import atom.service
import gdata.spreadsheet
import atom
import getopt
import sys
import string


class SimpleSpreadsheet:
    """
    Adapted from spreadsheetExample.py
    """

    def __init__(self, email='gregdingle@yahoo.com', password='008888'):
        self.gd_client = gdata.spreadsheet.service.SpreadsheetsService()
        self.gd_client.email = email
        self.gd_client.password = password
        self.gd_client.source = 'Spreadsheets GData Sample'
        self.gd_client.ProgrammaticLogin()
        self.curr_key = ''
        self.curr_wksht_id = ''
        self.list_feed = None

    def printSheets(self):
        # Get the list of spreadsheets
        feed = self.gd_client.GetSpreadsheetsFeed()
        for i, entry in enumerate(feed.entry):            
            print '%s %s' % (i, entry.title.text)

            # TODO: why this janky parsing of URLs for GUID?
            spreadsheet_id = feed.entry[i].id.text.split('/')[-1]

            worksheet_feed = self.gd_client.GetWorksheetsFeed(spreadsheet_id)
            for i, entry in enumerate(worksheet_feed.entry):
                print '\t%s %s' % (i, entry.title.text)


if __name__ == '__main__':
    s = SimpleSpreadsheet()
    s.printSheets()