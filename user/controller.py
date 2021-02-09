from .models import *
class Controller:

    def CartCount(self,user):
        self.cartcount = OrderItem.objects.filter(order__customer=user,order__status=False).count()

        return self.cartcount
    
    def TotalAmount(self,user):
        self.items = OrderItem.objects.filter(order__customer=user,order__status=False)
        self.total = 0
        self.totalpayamount = 0
        for i in self.items:
            self.total += i.subTotal()

        self.totalpayamount = self.total * 100
        return self.total, self.totalpayamount
