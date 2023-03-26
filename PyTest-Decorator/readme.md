Pytest, Python dilinde yazılmış bir test çerçevesidir ve test fonksiyonları için bir dizi özel dekoratör sağlar. Bazıları şunlardır:

@pytest.fixture: Bu dekoratör, test fonksiyonları tarafından kullanılmak üzere bir öğe oluşturur. Fixture, önceden koşulacak kod ve/veya verileri içeren ve testlerin her biri öncesinde çalıştırılan bir işlevdir.

@pytest.mark.parametrize: Bu dekoratör, aynı test kodunu farklı parametrelerle birden fazla kez çalıştırmak için kullanılır. Testin doğru çalışıp çalışmadığını kontrol etmek için farklı parametrelerle test etmek gerektiğinde bu dekoratör kullanılabilir.

@pytest.mark.skip: Bu dekoratör, test fonksiyonlarının atlanmasına neden olur. Testin çalıştırılmasını istemediğiniz veya henüz tamamlanmamış bir test için kullanılabilir.

@pytest.mark.xfail: Bu dekoratör, bir testin beklenen bir şekilde başarısız olacağını işaret eder. Testin başarısız olduğu, ancak henüz düzeltmediğiniz durumlarda bu dekoratör kullanılabilir.

@pytest.mark.timeout: Bu dekoratör, testin belirli bir sürede tamamlanması gerektiğini işaret eder. Testin sonsuza kadar çalışmasını önlemek için bu dekoratör kullanılabilir.

@pytest.mark.slow: Bu dekoratör, bir testin yavaş çalıştığını ve diğer testlerin zamanlamasını etkileyebileceğini belirtir. Bu dekoratör kullanılarak yavaş testlerin belirtilmesi, çalışma zamanı açısından optimize edilebilir.

Bu dekoratörlerin yanı sıra, Pytest ayrıca bazı özel dekoratörler de sağlar. Bunlar @pytest.fixture(scope="module"), @pytest.fixture(scope="session"), @pytest.fixture(autouse=True), @pytest.fixture(allow_module_level=True), @pytest.mark.usefixtures(), @pytest.mark.dependency(), @pytest.mark.flaky(), @pytest.mark.filterwarnings(), @pytest.mark.tryfirst() ve @pytest.mark.trylast() gibi dekoratörlerdir.