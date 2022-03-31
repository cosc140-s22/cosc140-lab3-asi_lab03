# COSC140 lab 3

## Answers to the five questions at the end of the lab description

1. shark = Product(name="stuffed shark", price= 45, minimum_age_appropriate=2, maximum_age_appropriate=43, description="soft, but with pointy teeth")

2. Product.objects.all()

3. >>> newProd = Product.objects.get(pk = 6)
>>> newProd.price = 22.50
>>> print(newProd)
   

4. newProd = Product.objects.get(pk = 6)
   newProd.delete()
   null
5. objects = Product.objects.filter(name__icontains='stuffed').filter(price__gt< 10)

## Lab feedback

 * How long did you spend on this lab?

 * What did you think about it?  What was good?  What could be improved?

## Feedback

Once you commit and submit your work to Github, I'll update this section with feedback.

