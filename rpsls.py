#coding:gbk
"""
�޽���
��һ��С��ĿRpsls
2020/4/14
"""
import random
# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����
def name_to_number(cboice_name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if cboice_name=="ʯͷ":
	    return 0#���ؽ��
    elif cboice_name=="ʷ����": 
	    return 1
    elif cboice_name=="��":
	    return 2
    elif cboice_name=="����":
	    return 3
    elif cboice_name=="����":
	    return 4
    else:
        return 5   
def number_to_name(comp_number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if comp_number==0:
      return "ʯͷ"
    elif comp_number==1:
      return "ʷ����"
    elif comp_number==2:
      return "��"
    elif comp_number==3:
      return "����"
    elif comp_number==4:
      return "����"
def rpsls(cboice_name):
    """
    �û�����������һ��ѡ�񣬸���Rpsls��Ϸ��������Ļ�������Ӧ�Ľ��
    """
    print("------------------------")# ���"-------- "���зָ�
    player_cboice=name_to_number(cboice_name)
    if player_cboice==5:
      print("Error: No Correct Name")
    else:
      print("����ѡ��Ϊ��%s"%(cboice_name))# ����name_to_number�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
      comp_number=random.randint(0,4)# ����random.randrange�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
      player_cboice_number=number_to_name(comp_number)	# ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
      print("���Ե�ѡ��Ϊ��%s"%(player_cboice_number))
      rule=comp_number-player_cboice 
      if rule==2 or rule==-3 or rule==1 or rule==-4:
        print("����Ӯ��")
      elif rule==0:
        print("���Ժ������һ����")
      else:
       print("��Ӯ��")  
print("��ӭʹ��Rpsls��Ϸ")
print("----------------")
print("����������ѡ��:")
cboice_name=input("")
rpsls(cboice_name)
