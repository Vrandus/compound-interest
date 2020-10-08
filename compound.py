
def interest(investment, years, interest):
     total_investment = 0
     total_generated = 0
     for i in range(years):
          total_investment += investment
          total_generated += investment
          total_generated = total_generated * interest
     
     print("total made: ", total_generated)
     print("total added: ", total_investment)
     print("made from interest: ", total_generated - total_investment)


interest(32000, 10, 1.06)