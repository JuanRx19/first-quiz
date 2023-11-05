package org.velezreyes.quiz.question6;

public class VendingMachineImpl implements VendingMachine {

  private static VendingMachineImpl instance;
  private int quarters;

  private VendingMachineImpl() {
    this.quarters = 0;
  }

  public static VendingMachineImpl getInstance() {
    if (instance == null) {
      instance = new VendingMachineImpl();
    }
    return instance;
  }

  @Override
  public void insertQuarter() {
    this.quarters++;
  }

  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
    if ("ScottCola".equals(name)) {
      if (quarters >= 3) {
        quarters -= 3;
        return new Drink() {
          @Override
          public String getName() {
            return "ScottCola";
          }

          @Override
          public boolean isFizzy() {
            return true;
          }
        };
      } else {
        throw new NotEnoughMoneyException();
      }
    } else if ("KarenTea".equals(name)) {
      if (quarters >= 4) {
        quarters -= 4;
        return new Drink() {
          @Override
          public String getName() {
            return "KarenTea";
          }

          @Override
          public boolean isFizzy() {
            return false;
          }
        };
      } else {
        throw new NotEnoughMoneyException();
      }
    } else {
      throw new UnknownDrinkException();
    }
  }

}
