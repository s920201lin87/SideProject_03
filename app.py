from abc import ABC,abstractmethod


class MemberDiscount(ABC):
    
    def __init__(self,
        member_name:str,
        member_email:str,
        member_phone:int):
        
        self.__member_name=member_name
        self.__member_email=member_email
        self.__member_phone=member_phone
        
    @property
    def member_name(self):
        return self.__member_name
    @property
    def member_email(self):
        return self.__member_email
    @property
    def member_phone(self):
        return self.__member_phone
    
    @abstractmethod
    def member_discount(self,price:float) -> float:
        pass
    
    def get_member_info(self) -> dict:
        return {
            "member_name":self.__member_name,
            "member_email":self.__member_email,
            "member_phone":self.__member_phone
        }

class VVIPMemberDiscount(MemberDiscount):
    def __init__(self,member_name:str, member_email:str, member_phone:int):
        
        super().__init__(
            member_name, 
            member_email, 
            member_phone)
        
        
    def member_discount(self,price:float) -> float:
        return price * 0.8
    
class VIPMemberDiscount(MemberDiscount):
    def __init__(self,member_name:str, member_email:str, member_phone:int):
        super().__init__(
            member_name,
            member_email,
            member_phone)
        

    def member_discount(self,price:float)-> float:
        return price * 0.9
    
class BasicMemberDiscount(MemberDiscount):
    def __init__(self,member_name:str,member_email:str,member_phone:int):
        super().__init__(member_name,member_email,member_phone)
        
        
    def member_discount(self,price:float)-> float:
        return price * 0.95
        
if __name__ == "__main__":
    # 建立不同等級會員，測試折扣機制
    vvip_member = VVIPMemberDiscount("Alice", "alice@example.com", 123456)
    vip_member  = VIPMemberDiscount("Bob", "bob@example.com", 987654)
    basic_member = BasicMemberDiscount("Charlie", "charlie@example.com", 555666)

    price = 1000
    print(f"VVIP: {vvip_member.member_name} 折扣後價格 = {vvip_member.member_discount(price)}")
    print(f"VIP : {vip_member.member_name} 折扣後價格 = {vip_member.member_discount(price)}")
    print(f"Basic: {basic_member.member_name} 折扣後價格 = {basic_member.member_discount(price)}")


