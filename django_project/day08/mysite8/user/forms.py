from django import forms
class MyRegForm(forms.Form):
    username=forms.CharField(label='用户名',
                             widget=forms.TextInput,
                             required=False,
                             initial='请输入')
    password=forms.CharField(label='密码',
                             # widget=forms.PasswordInput,
                             required=False,)
    password1=forms.CharField(label='重复密码',
                              widget=forms.PasswordInput)
    # age=forms.IntegerField(label='年龄')
    def clean_username(self):
        """此方法限定username必须大于等于六个字符"""
        uname=self.cleaned_data['username']
        if len(uname)<6:
            raise forms.ValidationError('用户名太短')
        return uname
    def clean(self):
        pwd1=self.cleaned_data['password']
        pwd2=self.cleaned_data['password1']
        if pwd1!=pwd2:
            raise forms.ValidationError('两次密码不一致')
        return self.cleaned_data
    # def clean_password(self):
    #     pwd=self.cleaned_data['password']
    #     if len(pwd)==0:
    #         raise forms.ValidationError('密码不能为空')
    #     return pwd